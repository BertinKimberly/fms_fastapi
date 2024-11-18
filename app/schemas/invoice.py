from pydantic import BaseModel, condecimal
from datetime import date
from typing import Optional

class InvoiceBase(BaseModel):
    client_id: int
    freelancer_id: int
    description: str
    amount: condecimal(max_digits=10, decimal_places=2)
    issue_date: date
    due_date: date
    status: str

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    id: int

    class Config:
        orm_mode = True
