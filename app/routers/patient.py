from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.patient import Patient

router = APIRouter(prefix="/patients")

def get_db():
    db = SessionLocal()
    yield db

@router.post("/")
def create_patient(name: str, phone: str, db: Session = Depends(get_db)):
    p = Patient(name=name, phone=phone)
    db.add(p)
    db.commit()
    return p

@router.get("/")
def search_patient(search: str = "", db: Session = Depends(get_db)):
    return db.query(Patient).filter(Patient.name.contains(search)).all()