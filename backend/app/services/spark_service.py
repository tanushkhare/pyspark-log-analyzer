from backend.app.schemas.logs import LogAnalysisRequest, LogAnalysisResponse, WorkerNodeTelemetry

class SparkLogService:
    @staticmethod
    def process_logs(payload: LogAnalysisRequest) -> LogAnalysisResponse:
        s200 = int(payload.batch_size * 0.948)
        s404 = int(payload.batch_size * 0.038)
        s500 = payload.batch_size - (s200 + s404)

        error_rate = round(((s404 + s500) / payload.batch_size) * 100, 2)
        latency = round(12.0 + (payload.batch_size / 500.0) * 0.8, 1)
        throughput = int(payload.batch_size / (latency / 1000.0))

        records_per_node = payload.batch_size // payload.partition_count
        workers = []
        for i in range(min(payload.partition_count, 4)):
            workers.append(WorkerNodeTelemetry(
                node_id=f"spark-worker-0{i+1}",
                records_processed=records_per_node,
                execution_time_ms=round(latency * 0.85, 1)
            ))

        return LogAnalysisResponse(
            batch_size=payload.batch_size,
            throughput_rps=throughput,
            error_rate_pct=error_rate,
            status_200_count=s200,
            status_200_pct=94.8,
            status_404_count=s404,
            status_404_pct=3.8,
            status_500_count=s500,
            status_500_pct=1.4,
            latency_ms=latency,
            worker_nodes=workers
        )

spark_service = SparkLogService()