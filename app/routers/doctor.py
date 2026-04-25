from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.doctor import Doctor

router = APIRouter(prefix="/doctors")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_doctor(name: str, specialization: str, db: Session = Depends(get_db)):
    doc = Doctor(name=name, specialization=specialization)
    db.add(doc)
    db.commit()
    return doc

@router.get("/")
def get_doctors(specialization: str = None, db: Session = Depends(get_db)):
    query = db.query(Doctor)
    if specialization:
        query = query.filter(Doctor.specialization == specialization)
    return query.all()

@router.put("/{id}")
def update_doctor(id: int, name: str, db: Session = Depends(get_db)):
    doc = db.query(Doctor).get(id)
    doc.name = name
    db.commit()
    return doc

@router.delete("/{id}")
def delete_doctor(id: int, db: Session = Depends(get_db)):
    doc = db.query(Doctor).get(id)
    db.delete(doc)
    db.commit()
    return {"msg": "Deleted"}

@router.patch("/{id}/toggle")
def toggle_doctor(id: int, db: Session = Depends(get_db)):
    doc = db.query(Doctor).get(id)
    doc.active = not doc.active
    db.commit()
    return doc