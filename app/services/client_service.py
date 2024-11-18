from sqlalchemy.orm import Session
from app.models.client import Client
from app.schemas.client import ClientCreate

def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def get_clients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Client).offset(skip).limit(limit).all()

def create_client(db: Session, client: ClientCreate):
    db_client = Client(
        name=client.name,
        email=client.email,
        phone=client.phone,
        address=client.address
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def update_client(db:Session,client_id:int,client_data:ClientCreate):
    db_client=db.query(Client).filter(Client.id==client_id).first()
    if db_client:
        db_client.name=client_data.name
        db_client.email=client_data.email
        db_client.phone=client_data.phone
        db_client.address=client_data.address
        db.commit()
        db.refresh(db_client)
        return db_client
    return None

def delete_client(db:Session,client_id:int):
    db_client=db.query(Client).filter(Client.id==client_id).first()
    if db_client:
        db.delete(db_client)
        db.commit()
        return db_client
    return None
