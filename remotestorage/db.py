""" create a database connection to a SQLite database with SQLmodel"""
import sqlmodel
from sqlmodel import SQLModel, create_engine, Field, Session, select
from sqlmodel.pool import StaticPool


class RemoteStorage(SQLModel, table=True):
    key: str = Field(default=None, index=True, primary_key=True)
    data: str = Field(default=None)

db_url = "sqlite:///remoteStorage.db"

engine = engine = create_engine(
        db_url,
        connect_args={"check_same_thread": False},
        echo=True,
        poolclass=StaticPool,
    )

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    return engine

