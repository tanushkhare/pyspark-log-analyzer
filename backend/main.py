from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers import logs
import uvicorn

app = FastAPI(
    title="PySpark Distributed Log Analyzer API",
    description="High-throughput log stream batching, status code classification, and RDD partition metrics.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(logs.router)

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "pyspark-log-analyzer"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)