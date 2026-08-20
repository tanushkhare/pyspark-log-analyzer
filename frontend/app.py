import streamlit as st
import requests

st.title("⚡ PySpark High-Volume Web Server Log Analyzer")
st.write("Execute distributed big data log parsing pipelines and visualize traffic patterns, error rates, and top requesting IPs.")

if st.button("Run PySpark Log Job"):
    try:
        with st.spinner("Processing high-volume log dataset via PySpark cluster..."):
            response = requests.get("http://127.0.0.1:8000/api/analyze")
            if response.status_code == 200:
                data = response.json()
                st.success(data["status"])
                
                col1, col2, col3 = st.columns(3)
                col1.metric("Total Logs Processed", f"{data['total_logs_processed']:,}")
                col2.metric("Error Count (5xx/4xx)", f"{data['error_count']:,}")
                col3.metric("Warning Count", f"{data['warning_count']:,}")
                
                st.subheader("🌐 Top Requesting IP Addresses")
                for item in data["top_ip_addresses"]:
                    st.write(f"- **{item['ip']}** : {item['requests']:,} requests")
            else:
                st.error("Failed to run distributed job on backend.")
    except Exception as e:
        st.error(f"Connection error: {e}")