from pydantic import BaseModel
from typing import Optional

class ClientBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int
    project_id: Optional[int] = None

    class Config:
        orm_mode = True
