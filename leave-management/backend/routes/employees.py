from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/")
def create_employee(data: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, data)

@router.get("/")
def get_employees(db: Session = Depends(get_db)):
    return crud.get_all_employees(db)