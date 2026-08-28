from fastapi import APIRouter, HTTPException
from backend.app.schemas.spark_schema import LogAnalysisRequest, LogAnalysisResponse
from backend.app.services.spark_service import spark_engine

router = APIRouter(prefix="/api/v1/logs", tags=["PySpark Log Analyzer"])

@router.post("/analyze", response_model=LogAnalysisResponse)
async def analyze_logs(payload: LogAnalysisRequest):
    try:
        result = spark_engine.process_logs(payload.batch_size, payload.partition_count, payload.log_format or "combined")
        return LogAnalysisResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/analyze", response_model=LogAnalysisResponse)
async def analyze_logs_get_fallback():
    result = spark_engine.process_logs(5000, 4, "combined")
    return LogAnalysisResponse(**result)
