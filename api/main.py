from typing import Annotated, Optional

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

# Dependency
def create_db_and_tables():
	SQLModel.metadata.create_all(engine)

def get_session():
	with Session(engine) as session:
		yield session

SessionDep = Annotated[Session, Depends(get_session)]

# FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
	return {"Hello": "World"}

# GET list of ALL diagnosis
@app.get("/diagnoses")
def read_all_diagnoses():
	codes = [{"code": "ABC", "name": "xyz"}]
	return codes


# GET all notes
# @app.get("/notes")
# def reat_notes(session: SessionDep) -> list[Note]


# CREATE a consultation note


# UPDATE an existing consulation note


# DELETE an exisitng consulation note


# GET list of all consultation notes


