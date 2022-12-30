from remotestorage.db import RemoteStorage, engine, Session, create_db_and_tables
from pathlib import Path

def test_create_row():

    create_db_and_tables()

    data = Path("tests/test_data.txt")
    content = RemoteStorage(id=0, key="key", data=data.read_text())
    
    with Session(engine) as session:
        session.merge(content)
        session.commit()
        
    with Session(engine) as session:
        content = session.query(RemoteStorage).filter(RemoteStorage.id == 0).first()
        assert content.key == "key"
        assert content.data == 'content\n '
        assert content.id == 0
    
    



    

