from sqlalchemy import Column, String, Integer, Float
from app.db.base_class import Base
from sqlalchemy.orm import relationship

class Freelancer(Base):
    __tablename__ = "freelancers"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=True)
    skills = Column(String, nullable=True)
    hourly_rate = Column(Float)
    invoices = relationship("Invoice", back_populates="freelancer")
