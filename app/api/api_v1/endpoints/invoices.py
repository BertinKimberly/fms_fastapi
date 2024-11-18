from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.invoice import Invoice, InvoiceCreate
from app.services.invoice_service import get_invoices, create_invoice, get_invoice
from app.db.session import get_db

router = APIRouter()

@router.get("/", response_model=List[Invoice])
def read_invoices(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    invoices = get_invoices(db, skip=skip, limit=limit)
    return invoices

@router.post("/", response_model=Invoice)
def create_new_invoice(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    return create_invoice(db, invoice)

@router.get("/{invoice_id}", response_model=Invoice)
def read_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = get_invoice(db, invoice_id)
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice
