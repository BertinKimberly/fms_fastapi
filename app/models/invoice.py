from sqlalchemy import Column, Integer, String, ForeignKey, Text, Numeric, Date
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    freelancer_id = Column(Integer, ForeignKey("freelancers.id"), nullable=False)
    description = Column(Text, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    issue_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    status = Column(String(20), nullable=False)

    client = relationship("Client", back_populates="invoices")
    freelancer = relationship("Freelancer", back_populates="invoices")
