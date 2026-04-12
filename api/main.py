from typing import Annotated, Optional
import json

from fastapi import FastAPI, HTTPException, Query, Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Diagnosis(SQLModel, table=True):
	id: int | None = Field(default=None, primary_key=True)
	code: str = Field(index=True)
	name: str = Field(default=None)

# class Note(SQLModel, table=True):
# 	id: int | None = Field(default=None, primary_key=True)
# 	desc: str = Field(index=True)
# 	date: str
# 	patient: str


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
@app.get("/diagnoses")
def read_all_diagnoses(
	session: Session = Depends(get_session),
	offset: int = 0,
	limit: int = Query(default=200, le=200)
) -> list[Diagnosis]:
	codes = session.exec(select(Diagnosis).offset(offset).limit(limit)).all()
	# hacky workaround for seeding db with codes just for the purposes of this demo
	if(len(codes) < 1):
		seed_db()
	return codes


# GET all notes
# @app.get("/notes")
# def reat_notes(session: SessionDep) -> list[Note]


# CREATE a consultation note


# UPDATE an existing consulation note


# DELETE an exisitng consulation note


# GET list of all consultation notes


