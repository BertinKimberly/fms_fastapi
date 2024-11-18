from sqlalchemy.orm import Session
from app.models.freelancer import Freelancer
from app.schemas.freelancer import FreelancerCreate

def get_freelancers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Freelancer).offset(skip).limit(limit).all()

def create_freelancer(db: Session, freelancer: FreelancerCreate):
    db_freelancer = Freelancer(
        first_name=freelancer.first_name,
        last_name=freelancer.last_name,
        email=freelancer.email,
        phone=freelancer.phone,
        skills=freelancer.skills,
        hourly_rate=freelancer.hourly_rate,
    )
    db.add(db_freelancer)
    db.commit()
    db.refresh(db_freelancer)
    return db_freelancer

def get_freelancer(db: Session, freelancer_id: int):
    return db.query(Freelancer).filter(Freelancer.id == freelancer_id).first()

def update_freelancer(db: Session, freelancer_id: int, freelancer: FreelancerCreate):
    db_freelancer = db.query(Freelancer).filter(Freelancer.id == freelancer_id).first()
    if not db_freelancer:
        return None
    for key, value in freelancer.dict().items():
        setattr(db_freelancer, key, value)
    db.commit()
    db.refresh(db_freelancer)
    return db_freelancer

def delete_freelancer(db: Session, freelancer_id: int):
    db_freelancer = db.query(Freelancer).filter(Freelancer.id == freelancer_id).first()
    if not db_freelancer:
        return False
    db.delete(db_freelancer)
    db.commit()
    return True
