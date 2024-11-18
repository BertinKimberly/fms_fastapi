from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.freelancer import Freelancer, FreelancerCreate
from app.services.freelancer_service import (
    get_freelancers,
    create_freelancer,
    get_freelancer,
    update_freelancer,
    delete_freelancer,
)
from app.db.session import get_db

router = APIRouter()

@router.get("/", response_model=List[Freelancer])
def read_freelancers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of freelancers.
    """
    return get_freelancers(db, skip=skip, limit=limit)

@router.post("/", response_model=Freelancer)
def create_new_freelancer(freelancer: FreelancerCreate, db: Session = Depends(get_db)):
    """
    Create a new freelancer.
    """
    return create_freelancer(db, freelancer)

@router.get("/{freelancer_id}", response_model=Freelancer)
def read_freelancer(freelancer_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single freelancer by ID.
    """
    freelancer = get_freelancer(db, freelancer_id)
    if freelancer is None:
        raise HTTPException(status_code=404, detail="Freelancer not found")
    return freelancer

@router.put("/{freelancer_id}", response_model=Freelancer)
def update_existing_freelancer(
    freelancer_id: int, freelancer: FreelancerCreate, db: Session = Depends(get_db)
):
    """
    Update a freelancer's details.
    """
    updated_freelancer = update_freelancer(db, freelancer_id, freelancer)
    if updated_freelancer is None:
        raise HTTPException(status_code=404, detail="Freelancer not found")
    return updated_freelancer

@router.delete("/{freelancer_id}")
def delete_freelancer_endpoint(freelancer_id: int, db: Session = Depends(get_db)):
    """
    Delete a freelancer by ID.
    """
    success = delete_freelancer(db, freelancer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Freelancer not found")
    return {"message": "Freelancer deleted successfully"}
