from sqlalchemy.orm import Session
from models import Employee, LeaveRequest
from schemas import EmployeeCreate, LeaveCreate, LeaveUpdate

def create_employee(db: Session, data: EmployeeCreate):
    emp = Employee(**data.dict())
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp

def get_all_employees(db: Session):
    return db.query(Employee).all()

def apply_leave(db: Session, data: LeaveCreate):
    overlap = db.query(LeaveRequest).filter(
        LeaveRequest.employee_id == data.employee_id,
        LeaveRequest.status != "Rejected",
        LeaveRequest.start_date <= data.end_date,
        LeaveRequest.end_date >= data.start_date,
    ).first()
    if overlap:
        raise ValueError("Overlapping leave request exists")
    leave = LeaveRequest(**data.dict())
    db.add(leave)
    db.commit()
    db.refresh(leave)
    return leave

def get_all_leaves(db: Session):
    return db.query(LeaveRequest).all()

def get_employee_leaves(db: Session, employee_id: int):
    return db.query(LeaveRequest).filter(
        LeaveRequest.employee_id == employee_id
    ).all()

def update_leave(db: Session, leave_id: int, data: LeaveUpdate):
    leave = db.query(LeaveRequest).filter(
        LeaveRequest.id == leave_id
    ).first()
    if not leave:
        raise ValueError("Leave request not found")
    if leave.status != "Pending":
        raise ValueError("Only pending requests can be edited")
    for k, v in data.dict(exclude_unset=True).items():
        setattr(leave, k, v)
    db.commit()
    db.refresh(leave)
    return leave

def delete_leave(db: Session, leave_id: int):
    leave = db.query(LeaveRequest).filter(
        LeaveRequest.id == leave_id
    ).first()
    if not leave:
        raise ValueError("Leave request not found")
    if leave.status != "Pending":
        raise ValueError("Only pending requests can be deleted")
    db.delete(leave)
    db.commit()
    return {"message": "Deleted successfully"}

def admin_action(db: Session, leave_id: int, status: str):
    leave = db.query(LeaveRequest).filter(
        LeaveRequest.id == leave_id
    ).first()
    if not leave:
        raise ValueError("Leave request not found")
    if leave.status != "Pending":
        raise ValueError("Already processed")
    leave.status = status
    db.commit()
    db.refresh(leave)
    return leave    