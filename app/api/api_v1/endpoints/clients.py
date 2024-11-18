from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.client import Client, ClientCreate
from app.services.client_service import delete_client, get_clients, create_client, get_client, update_client
from app.db.session import get_db

router = APIRouter()

@router.get("/", response_model=List[Client])
def read_clients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    clients = get_clients(db, skip=skip, limit=limit)
    return clients

@router.post("/", response_model=Client)
def create_new_client(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db, client)

@router.get("/{client_id}", response_model=Client)
def read_client(client_id: int, db: Session = Depends(get_db)):
    client = get_client(db, client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client


@router.put("/{client_id}",response_model=Client)
def update_client_details(client_id:int,client_data:ClientCreate,db:Session=Depends(get_db)):
    updated_client=update_client(db,client_id,client_data)
    if not update_client:
        raise HTTPException(status_code=404,detail="Client not found")
    
@router.delete("/{client_id}",response_model=Client)
def delete_client_account(client_id:int,db:Session=Depends(get_db)):
    deleted_client=delete_client(db,client_id)    
    if not deleted_client:
        raise HTTPException(status_code=404,detail="Client not found")
    return deleted_client