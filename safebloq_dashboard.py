import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
from datetime import datetime
import random

st.set_page_config(page_title="Safebloq Dashboard", layout="wide")

# --- Brand Colors ---
PRIMARY_COLOR = "#1A3C5A"
SECONDARY_COLOR = "#00C4B3"
BG_COLOR = "#F8FAFC"

st.markdown(f"""
    <style>
        .main {{
            background-color: {BG_COLOR};
        }}
        .css-1rs6os.edgvbvh3 {{
            background-color: {PRIMARY_COLOR};
        }}
        .stButton > button {{
            background-color: {SECONDARY_COLOR};
            color: white;
        }}
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.image("https://i.ibb.co/BwFdVBP/safebloq-logo.png", width=180)
menu = st.sidebar.radio("Navigation", ["Dashboard", "Devices", "Reports"])

# --- Dummy Data ---
alerts = pd.DataFrame({
    "Time": pd.date_range(end=datetime.now(), periods=5, freq='h'),
    "Alert": ["Unauthorized login", "Suspicious file", "Blocked IP", "Phishing email", "Malware detected"],
    "Severity": ["High", "Medium", "High", "Low", "Critical"]
})

devices = pd.DataFrame({
    "Device Name": ["Laptop-A1", "POS-Terminal-2", "Server-3", "Phone-B4"],
    "Status": ["Secure", "Under Review", "Secure", "At Risk"],
    "Last Check-in": [datetime.now().strftime("%Y-%m-%d %H:%M")]*4
})

security_score = random.randint(65, 95)

# --- Dashboard Page ---
if menu == "Dashboard":
    st.title("🔐 Safebloq Zero Trust Dashboard")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Security Score", f"{security_score} / 100")
    col2.metric("Active Alerts", str(len(alerts)))
    col3.metric("Devices Monitored", str(len(devices)))

    st.subheader("📊 Threat Trends")
    fig, ax = plt.subplots()
    threats = [5, 10, 8, 4, 12]
    dates = pd.date_range(end=datetime.now(), periods=5).strftime("%b %d")
    ax.plot(dates, threats, marker='o', color=SECONDARY_COLOR)
    ax.set_ylabel("Detections")
    st.pyplot(fig)

    st.subheader("🚨 Recent Alerts")
    st.dataframe(alerts)

# --- Devices Page ---
elif menu == "Devices":
    st.title("🖥️ Monitored Devices")
    st.table(devices)

# --- Reports Page ---
elif menu == "Reports":
    st.title("📄 Generate Daily Report")

    report_content = f"""
    Safebloq Security Report - {datetime.now().strftime('%Y-%m-%d')}

    Security Score: {security_score}
    Active Alerts: {len(alerts)}
    Devices Monitored: {len(devices)}

    Recent Alerts:
    {alerts.to_string(index=False)}
    """

    b64 = base64.b64encode(report_content.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="Safebloq_Report.txt">📥 Download Report</a>'
    st.markdown(href, unsafe_allow_html=True)
