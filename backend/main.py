from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import logs

app = FastAPI(
    title="PySpark High-Volume Web Server Log Analyzer API",
    version="1.0.0",
    description="Distributed data processing backend using PySpark and FastAPI."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(logs.router)

@app.get("/")
def read_root():
    return {"message": "PySpark Log Analyzer Backend is online!"}