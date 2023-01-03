from remotestorage.db import Session, engine, RemoteStorage, select 


def getByIdOp(id):

    with Session(engine) as session:
            allItems = session.exec(
                select(
                    RemoteStorage.key,
                    RemoteStorage.data
                    )
                ).all()

    return allItems[id]

def getAllItemsOp():
    with Session(engine) as session:
        allItems = session.exec(
            select(
                RemoteStorage.key,
                RemoteStorage.data
                )
            ).all()
        
        return allItems

def getItemOp(key):
    with Session(engine) as session:
        statement = select(RemoteStorage).where(RemoteStorage.key == key)
        result = session.exec(statement).first()
        return result

def setItemOp(remoteStorage: RemoteStorage):
    
    with Session(engine) as session:
        session.merge(remoteStorage)
        session.commit()
    return remoteStorage

def lengthOp():
    with Session(engine) as session:
        statement = select(RemoteStorage)
        results = session.exec(statement).all()
        return {"length": len(results)}