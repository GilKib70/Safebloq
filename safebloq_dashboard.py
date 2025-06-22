import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Safebloq MVP", layout="wide")

st.title("🛡️ Safebloq - Zero Trust Cybersecurity for SMBs")
st.markdown("A simple dashboard MVP showcasing real-time security visibility for small businesses.")

st.header("🚨 Detected Security Events")
data = {
    "Time": ["09:01", "09:14", "09:26", "10:05"],
    "Event Type": ["Phishing Attempt", "Suspicious Login", "Ransomware Blocked", "USB Access Denied"],
    "Device": ["Laptop-01", "Mobile-Admin", "Desktop-Accounting", "Tablet-Warehouse"],
    "Status": ["Blocked", "Alert", "Quarantined", "Blocked"]
}
df = pd.DataFrame(data)
st.dataframe(df)

st.header("📊 Incident Overview")
chart_data = pd.DataFrame({
    "Blocked": [12, 18, 24, 30],
    "Quarantined": [5, 6, 4, 8],
    "Alerts": [3, 4, 5, 7]
}, index=["Mon", "Tue", "Wed", "Thu"])

st.bar_chart(chart_data)

st.header("✅ Security Health")
col1, col2, col3 = st.columns(3)
col1.metric("Devices Secured", "56", "+6")
col2.metric("Threats Blocked", "102", "+12")
col3.metric("Users Protected", "43", "+3")

st.info("This MVP demo shows simulated activity. Real-time integration will occur in beta release.")
