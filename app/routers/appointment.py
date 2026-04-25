from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.appointment import Appointment

router = APIRouter(prefix="/appointments")

def get_db():
    db = SessionLocal()
    yield db

@router.post("/")
def create_appointment(data: dict, db: Session = Depends(get_db)):
    a = Appointment(**data)
    db.add(a)
    db.commit()
    return a

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return db.query(Appointment).all()

@router.get("/doctor/{id}")
def by_doctor(id: int, db: Session = Depends(get_db)):
    return db.query(Appointment).filter(Appointment.doctor_id == id).all()

@router.get("/patient/{id}")
def by_patient(id: int, db: Session = Depends(get_db)):
    return db.query(Appointment).filter(Appointment.patient_id == id).all()

@router.patch("/{id}/cancel")
def cancel(id: int, db: Session = Depends(get_db)):
    a = db.query(Appointment).get(id)
    a.status = "Cancelled"
    db.commit()
    return a