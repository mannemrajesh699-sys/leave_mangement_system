# backend/routes/leaves.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas

router = APIRouter(prefix="/leaves", tags=["Leaves"])

@router.post("/")
def apply(data: schemas.LeaveCreate, db: Session = Depends(get_db)):
    try:    return crud.apply_leave(db, data)
    except ValueError as e: raise HTTPException(400, str(e))

@router.get("/")
def all_leaves(db: Session = Depends(get_db)):
    return crud.get_all_leaves(db)

@router.get("/employee/{emp_id}")
def my_leaves(emp_id: int, db: Session = Depends(get_db)):
    return crud.get_employee_leaves(db, emp_id)
@router.put("/{leave_id}")
def update(leave_id: int, data: schemas.LeaveUpdate, db: Session = Depends(get_db)):
    try:    return crud.update_leave(db, leave_id, data)
    except ValueError as e: raise HTTPException(400, str(e))

@router.delete("/{leave_id}")
def delete(leave_id: int, db: Session = Depends(get_db)):
    return crud.delete_leave(db, leave_id)

@router.patch("/{leave_id}/status")
def admin_action(leave_id: int, data: schemas.LeaveStatusUpdate, db: Session = Depends(get_db)):
    try:    return crud.admin_action(db, leave_id, data.status)
    except ValueError as e: raise HTTPException(400, str(e))
