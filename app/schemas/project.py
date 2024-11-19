from pydantic import BaseModel
from enum import Enum
from typing import Optional




class ProjectBase(BaseModel):
    name: str
    field: str
    description: str
    budget: int

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True
