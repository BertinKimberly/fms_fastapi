from pydantic import BaseModel

class FreelancerBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str | None = None
    skills: str | None = None
    hourly_rate: float | None = None

class FreelancerCreate(FreelancerBase):
    pass

class Freelancer(FreelancerBase):
    id: int

    class Config:
        orm_mode = True
