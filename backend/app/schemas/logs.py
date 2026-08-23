from pydantic import BaseModel, Field
from typing import List

class LogAnalysisRequest(BaseModel):
    batch_size: int = Field(..., ge=100, le=100000)
    partition_count: int = Field(..., ge=1, le=64)
    log_format: str

class WorkerNodeTelemetry(BaseModel):
    node_id: str
    records_processed: int
    execution_time_ms: float

class LogAnalysisResponse(BaseModel):
    batch_size: int
    throughput_rps: int
    error_rate_pct: float
    status_200_count: int
    status_200_pct: float
    status_404_count: int
    status_404_pct: float
    status_500_count: int
    status_500_pct: float
    latency_ms: float
    worker_nodes: List[WorkerNodeTelemetry]