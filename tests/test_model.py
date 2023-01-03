from remotestorage.db import RemoteStorage, engine, Session, create_db_and_tables
from pathlib import Path
from remotestorage.operations import getByIdOp, getAllItemsOp, getItemOp, setItemOp, lengthOp

def test_create_row():

    create_db_and_tables()

    data = Path("tests/test_data.txt")
    content = RemoteStorage(key="key", data=data.read_text())
    
    with Session(engine) as session:
        session.merge(content)
        session.commit()
        
    with Session(engine) as session:
        content = session.query(RemoteStorage).filter(RemoteStorage.key == "key").first()
        assert content.key == "key"
        assert content.data == 'content\n '
    
    
def test_getById():
    content = getByIdOp(0)
    assert content.key == "key"
    assert content.data == 'content\n '

def test_getAllItems():
    allItems = getAllItemsOp()
    assert allItems[0].key == "key"
    assert allItems[0].data == 'content\n '

def test_getItem():
    content = getItemOp("key")
    assert content.key == "key"
    assert content.data == 'content\n '

def test_setItem():
    content = setItemOp(RemoteStorage(key="key", data='content\n '))
    assert content.key == "key"
    assert content.data == 'content\n '

def test_length():
    length = lengthOp()
    assert length["length"] >= 1