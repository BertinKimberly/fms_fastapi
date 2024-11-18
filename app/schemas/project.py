from pydantic import BaseModel
from enum import Enum
from typing import Optional

class FieldType(str, Enum):
    TRANSPORT = "Transport"
    AGRICULTURE = "Agriculture"
    TRADE = "Trade"
    ENVIRONMENTAL_PROTECTION = "Environmental Protection"

class ProjectBase(BaseModel):
    name: str
    field: FieldType
    description: str
    budget: int

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True
