from typing import Annotated, Optional
from datetime import datetime
import json

from fastapi import FastAPI, HTTPException, Query, Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select, or_
from pydantic import BaseModel


class Diagnosis(SQLModel, table=True):
	id: int | None = Field(default=None, primary_key=True)
	code: str = Field(index=True)
	name: str = Field(default=None)

class Note(SQLModel, table=True):
	id: int | None = Field(default=None, primary_key=True)
	desc: str = Field(index=True)
	patient: str
	diagnosis_id: int | None = Field(default=None, foreign_key="diagnosis.id")

class CreateNoteRequest(BaseModel):
	desc: str
	patient: str
	diagnosis_id: int

# class UpdateNoteRequest(BaseModel):
# 	id: int
# 	desc: str
# 	patient: str
# 	diagnosis_id: int

class NoteResponse(BaseModel):
	id: int
	desc: str
	patient: str
	diagnosis_id: int
	created_at: datetime
	updated_at: datetime

	class Config:
		from_attributes = True


#Database setup
SQL_FILE_NAME="database.db"
DATABASE_URL = f"sqlite:///{SQL_FILE_NAME}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)
SQLModel.metadata.create_all(engine)


def create_db_and_tables():
	SQLModel.metadata.create_all(engine)


def get_session():
	with Session(engine) as session:
		yield session


SessionDep = Annotated[Session, Depends(get_session)]
app = FastAPI()


def seed_db():
	with open('code_dump.json', 'r') as dump_file:
		code_data = json.load(dump_file)

	for code_entry in code_data:
		with Session(engine) as session:
			new_code = Diagnosis(name=code_entry["name"], code=code_entry["code"])
			session.add(new_code)		
			session.commit()

@app.on_event("startup")
def on_startup():
	create_db_and_tables()


@app.get("/")
def read_root():
	return {"Hello": "World"}


# GET list of ALL diagnosis
@app.get("/diagnosis", summary="Retreive all diagnosis codes")
def read_all_diagnoses(
	session: Session = Depends(get_session),
	offset: int = 0,
	limit: int = Query(default=200, le=200),
	search: str = Query(default=None, description="Searches for diagnosis based on text in name or code")
) -> list[Diagnosis]:
	codes = session.exec(select(Diagnosis).offset(offset).limit(limit)).all()
	# hacky workaround for seeding db with codes just for the purposes of this demo
	if(len(codes) < 1):
		seed_db()
	if search:
		codes = session.exec(select(Diagnosis).filter(or_(Diagnosis.code.contains(search), Diagnosis.name.contains(search))).offset(offset).limit(limit)).all()
	return codes


# GET all notes
@app.get("/consultation")
def read_notes(session: Session = Depends(get_session)) -> list[Note]:
	notes = session.exec(select(Note)).all()
	return notes


# CREATE a consultation note
@app.post("/consultation", response_model=NoteResponse)
def create_note(request_data: CreateNoteRequest, session: Session = Depends(get_session)):
	selected_diagnosis = session.get(Diagnosis, request_data.diagnosis_id)
	if selected_diagnosis is None:
		raise HTTPException(
			status_code=402,
			detail=f"The associated diagnosis for this consulation note is invalid. No diagnosis with ID {request_data.diagnosis_id} could be found."
		)

	new_note = Note.model_validate(request_data)
	session.add(new_note)
	session.commit()	
	session.refresh(new_note)
	return new_note