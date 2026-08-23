from fastapi import APIRouter
from backend.app.schemas.logs import LogAnalysisRequest, LogAnalysisResponse
from backend.app.services.spark_service import spark_service

router = APIRouter(prefix="/api/v1/logs", tags=["PySpark Log Analyzer Engine"])

@router.post("/analyze", response_model=LogAnalysisResponse)
async def analyze_log_batch(payload: LogAnalysisRequest):
    return spark_service.process_logs(payload)