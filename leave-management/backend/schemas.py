from pydantic import BaseModel, validator
from datetime import date
from typing import Optional

class EmployeeCreate(BaseModel):
    name: str
    email: str
    role: str = "employee"

class EmployeeOut(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        orm_mode = True

class LeaveCreate(BaseModel):
    employee_id: int
    leave_type: str
    start_date: date
    end_date: date
    reason: Optional[str] = None

    @validator("start_date")
    def no_past_dates(cls, v):
        if v < date.today():
            raise ValueError("Cannot apply leave for past dates")
        return v

    @validator("end_date")
    def end_after_start(cls, v, values):
        if "start_date" in values and v < values["start_date"]:
            raise ValueError("end_date must be after start_date")
        return v

class LeaveUpdate(BaseModel):
    leave_type: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    reason: Optional[str] = None

class LeaveStatusUpdate(BaseModel):
    status: str
