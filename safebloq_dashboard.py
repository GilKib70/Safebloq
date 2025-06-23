
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- PAGE CONFIG ---
st.set_page_config(page_title="Safebloq Dashboard", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
        body {
            background-color: #f0f8ff;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .stMetric {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 10px;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🔐 Safebloq Security Dashboard")
st.markdown("Stay on top of your SME's cybersecurity posture in real time.")

# --- SECURITY SCORE ---
st.subheader("Security Score")
score = 78
st.progress(score / 100)

# --- THREAT TRENDS BAR CHART ---
st.subheader("Threat Trends (Last 3 Months)")
data = {
    'Month': ['April', 'May', 'June'],
    'Malware': [12, 18, 9],
    'Phishing': [7, 10, 5],
    'Device Attacks': [5, 7, 4],
}
df = pd.DataFrame(data).set_index('Month')
st.bar_chart(df)

# --- ENDPOINT STATUS ---
st.subheader("Endpoint Security Status")
col1, col2, col3 = st.columns(3)
col1.metric("Safe", "42")
col2.metric("Soft", "7")
col3.metric("Red", "2")

# --- LIVE ALERTS ---
st.subheader("Live Alerts")
alerts = [
    {"Device": "Laptop-01", "Issue": "Phishing Attempt Blocked"},
    {"Device": "Tablet-05", "Issue": "Unpatched OS Detected"},
    {"Device": "Server-02", "Issue": "New Admin Login Detected"},
]
for alert in alerts:
    st.warning(f"{alert['Device']}: {alert['Issue']}")

# --- ASSET TABLE ---
st.subheader("Assets Overview")
assets = pd.DataFrame({
    "Device": ["Laptop-01", "Tablet-05", "Server-02"],
    "User": ["Alice", "Bob", "Admin"],
    "Status": ["Safe", "Soft", "Red"],
})
st.dataframe(assets)
