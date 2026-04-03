from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Employee(Base):
    __tablename__ = "employees"
    id     = Column(Integer, primary_key=True, index=True)
    name   = Column(String(100), nullable=False)
    email  = Column(String(150), unique=True, nullable=False)
    role   = Column(String(20), default="employee")
    leaves = relationship("LeaveRequest", back_populates="employee")

class LeaveRequest(Base):
    __tablename__ = "leave_requests"
    id          = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    leave_type  = Column(String(50), nullable=False)
    start_date  = Column(Date, nullable=False)
    end_date    = Column(Date, nullable=False)
    reason      = Column(Text)
    status      = Column(String(20), default="Pending")
    employee    = relationship("Employee", back_populates="leaves")