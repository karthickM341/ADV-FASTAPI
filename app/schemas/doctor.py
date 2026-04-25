from pydantic import BaseModel

class DoctorCreate(BaseModel):
    name: str
    specialization: str

class DoctorResponse(DoctorCreate):
    id: int
    active: bool

    class Config:
        orm_mode = True