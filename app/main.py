# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .controller import banheiro_controller

app = FastAPI(
    title="API Toilet Map",
    description="API para encontrar e avaliar banheiros",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include router
app.include_router(
    banheiro_controller.router,
    prefix="/api/v1",
    tags=["Bathrooms"]
)