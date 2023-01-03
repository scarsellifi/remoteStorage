"""Webapp for remoteStorage"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from remotestorage.db import engine, Session, RemoteStorage, select, create_db_and_tables
import uvicorn
from remotestorage.operations import getByIdOp, getAllItemsOp, getItemOp, setItemOp, lengthOp

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
    return lengthOp()

@app.get("/{token}/getAllItems")
def getAllItems(token: str):
    if token != TOKEN:
        return {"error": "invalid token"}
    return getAllItemsOp()

@app.get("/{token}/key/{id}")
def key(token: str, id: int):
    print(id)
    if token != TOKEN:
        return {"error": "invalid token"}
    return getByIdOp(id)
        
@app.post("/{token}/getItem")
def key(token: str, remoteStorage: RemoteStorage):
    if token != TOKEN:
        return {"error": "invalid token"}
    return getItemOp(remoteStorage.key)

@app.post("/{token}/setItem")
def setItem(token: str, remoteStorage: RemoteStorage):
    if token != TOKEN:
        return {"error": "invalid token"}
    return setItemOp(remoteStorage)

def start():
    uvicorn.run(app, host="0.0.0.0", port=8000)
