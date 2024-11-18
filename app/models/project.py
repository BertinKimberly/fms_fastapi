from sqlalchemy import Column, String, Integer, Enum, Text
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum

class FieldType(enum.Enum):
    TRANSPORT = "Transport"
    AGRICULTURE = "Agriculture"
    TRADE = "Trade"
    ENVIRONMENTAL_PROTECTION = "Environmental Protection"

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    field = Column(Enum(FieldType), nullable=False)
    description = Column(Text, nullable=False)
    budget = Column(Integer, nullable=False)

    clients = relationship("Client", back_populates="project")
