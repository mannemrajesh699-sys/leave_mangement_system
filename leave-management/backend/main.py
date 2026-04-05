from fastapi import FastAPI
from database import engine, Base
from routes import employees, leaves

app = FastAPI(title="Leave Management System")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(employees.router)
app.include_router(leaves.router)

@app.get("/")
def root():
    return {"message": "Leave Management System API is running"}