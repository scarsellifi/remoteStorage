"""Webapp for remoteStorage"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from remotestorage.db import engine, Session, RemoteStorage, select, create_db_and_tables
import uvicorn

create_db_and_tables()

app = FastAPI()

origins = [
    "*",
]

TOKEN = "ABCDEFGHI"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{token}/")
def home(token: str):
    if token != TOKEN:
        return {"error": "invalid token"}
    return {"message": "Hello from remotestorage"}

@app.get("/{token}/length")
def length(token: str):
    if token != TOKEN:
        return {"error": "invalid token"}
    with Session(engine) as session:
        statement = select(RemoteStorage)
        results = session.exec(statement).all()
        return {"length": len(results)}

@app.get("/{token}/getAllItem")
def getAllItem(token: str):
    if token != TOKEN:
        return {"error": "invalid token"}
    with Session(engine) as session:
        keys = session.exec(
            select(
                RemoteStorage.id,
                RemoteStorage.key
                )
            ).all()
        
        return keys

@app.get("{token}/key/{id}")
def key(token: str, id: int):
    if token != TOKEN:
        return {"error": "invalid token"}
    with Session(engine) as session:
        statement = select(RemoteStorage).where(RemoteStorage.id == id)
        result = session.exec(statement).first()
        return result
        
@app.post("{token}/getItem")
def key(token: str, remoteStorage: RemoteStorage):
    if token != TOKEN:
        return {"error": "invalid token"}
    with Session(engine) as session:
        statement = select(RemoteStorage).where(RemoteStorage.key == remoteStorage.key)
        result = session.exec(statement).first()
        return result

@app.post("{token}/setItem")
def setItem(token: str, remoteStorage: RemoteStorage):
    if token != TOKEN:
        return {"error": "invalid token"}
    with Session(engine) as session:
        session.merge(remoteStorage)
        session.commit()
    return remoteStorage

def start():
    uvicorn.run(app, host="0.0.0.0", port=8000)
