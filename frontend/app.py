import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="PySpark Log Analyzer", layout="wide")

st.title("⚡ Distributed PySpark Log Analytics Engine")
st.markdown("Distributed RDD/DataFrame batch log aggregation, error spike detection, and cluster throughput monitoring.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Spark Job Parameters")
    batch_size = st.slider("Log Line Batch Size", 1000, 50000, 10000, step=1000)
    partitions = st.slider("Spark Partitions", 1, 16, 4)
    log_format = st.selectbox("Log Ingestion Format", ["combined", "json", "common"])

    if st.button("Dispatch Spark Map-Reduce Job", type="primary"):
        with st.spinner("Executing distributed transformations across partitions..."):
            try:
                res = requests.post(
                    "http://localhost:8000/api/v1/logs/analyze",
                    json={"batch_size": batch_size, "partition_count": partitions, "log_format": log_format},
                    timeout=5
                )
                if res.status_code == 200:
                    st.session_state["p11_result"] = res.json()
                    st.success("Spark Job Finished!")
                else:
                    st.error(f"Spark Job Error: {res.text}")
            except Exception:
                st.warning("Backend offline. Running simulated distributed calculation.")
                st.session_state["p11_result"] = {
                    "job_id": "SPARK-SIM801",
                    "records_processed": batch_size,
                    "partition_count": partitions,
                    "throughput_eps": round((batch_size * partitions * 12.5) / 1.5, 2),
                    "status_codes": {
                        "status_200": int(batch_size * 0.88),
                        "status_304": int(batch_size * 0.05),
                        "status_404": int(batch_size * 0.04),
                        "status_500": int(batch_size * 0.03)
                    },
                    "error_rate_pct": 7.0,
                    "error_spike_detected": True,
                    "top_flagged_endpoints": [
                        {"endpoint": "/api/v1/auth/login", "errors": 34, "dominant_code": 500},
                        {"endpoint": "/static/bundle.js", "errors": 45, "dominant_code": 404}
                    ],
                    "timestamp": "2026-08-28T10:15:00Z"
                }

with col2:
    if "p11_result" in st.session_state:
        res = st.session_state["p11_result"]
        st.subheader(f"Job Telemetry: {res['job_id']}")
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Logs Processed", f"{res['records_processed']:,}")
        m2.metric("Throughput (EPS)", f"{res['throughput_eps']:,.1f}")
        m3.metric("Error Rate", f"{res['error_rate_pct']}%", delta="SPIKE DETECTED" if res["error_spike_detected"] else "NOMINAL")
        
        if res["error_spike_detected"]:
            st.error("🚨 ALERT: Elevated 5xx/4xx Error Spike Detected Across Cluster Nodes")
        else:
            st.success("✅ Cluster HTTP Error Rate Operating Within 2% Target SLA")
            
        codes = res["status_codes"]
        status_df = pd.DataFrame({
            "HTTP Status Code": ["200 OK", "304 Not Modified", "404 Not Found", "500 Internal Error"],
            "Count": [codes["status_200"], codes["status_304"], codes["status_404"], codes["status_500"]]
        })
        fig = px.bar(status_df, x="HTTP Status Code", y="Count", color="HTTP Status Code", title="Status Code Frequency Distribution")
        st.plotly_chart(fig, use_container_width=True)
