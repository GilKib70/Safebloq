import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random
from datetime import datetime

# Set page config
st.set_page_config(page_title="Safebloq", layout="wide")

# --------- Styling ---------
st.markdown("""
    <style>
    body {
        color: white;
        background-color: #0e1117;
    }
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1e1e2f;
        color: white;
        padding: 1rem;
        border-radius: 8px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #00aaff;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# --------- Simulated Data ---------
security_score = random.randint(50, 100)
active_threats = random.randint(0, 15)
phishing_attempts = random.randint(0, 10)
outbound_denials = random.randint(0, 20)
unsafe_devices = random.randint(0, 5)

# --------- Header ---------
st.title("Safebloq")

# --------- Security Score Gauge ---------
st.subheader("Security Score")
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=security_score,
    domain={'x': [0, 1], 'y': [0, 1]},
    gauge={
        'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "white"},
        'bar': {'color': "white"},
        'steps': [
            {'range': [0, 40], 'color': "red"},
            {'range': [40, 70], 'color': "orange"},
            {'range': [70, 100], 'color': "green"}
        ],
        'threshold': {
            'line': {'color': "white", 'width': 4},
            'thickness': 0.75,
            'value': security_score
        }
    }
))
fig.update_layout(
    height=300,
    margin=dict(t=0, b=0, l=0, r=0),
    paper_bgcolor="#0e1117",
    font=dict(color="white")
)
st.plotly_chart(fig, use_container_width=True)

# --------- Live Alerts Overview ---------
st.subheader("Live Alerts Overview")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Threats", active_threats)
col2.metric("Phishing Attempts", phishing_attempts)
col3.metric("Outbound Denials", outbound_denials)
col4.metric("Unsafe Devices", unsafe_devices)

# --------- Tabs ---------
tabs = st.tabs(["Devices", "Reports", "Invite Team", "Support"])

# Devices Tab
with tabs[0]:
    st.subheader("Connected Devices")
    st.dataframe(pd.DataFrame({
        "Device Name": ["Laptop-01", "Server-02", "Mobile-03"],
        "Status": ["Secure", "Threat Detected", "Outdated"],
        "Last Seen": ["2025-06-30", "2025-06-29", "2025-06-28"]
    }))

# Reports Tab
with tabs[1]:
    st.subheader("Compliance Reports")
    st.info("Download latest GDPR, ISO27001, and Cyber Essentials reports.")
    st.download_button("Download GDPR Report", data="Fake GDPR content", file_name="gdpr_report.pdf")

# Invite Team Tab
with tabs[2]:
    st.subheader("Invite Team Members")
    email = st.text_input("Team Member Email")
    if st.button("Send Invite"):
        st.success(f"Invitation sent to {email}")

# Support Tab
with tabs[3]:
    st.subheader("Support")
    with st.expander("User Docs"):
        st.write("Instructions on how to use Safebloq")
    with st.expander("Support Docs"):
        st.write("Troubleshooting and technical references")

# Footer
st.markdown("---")
st.caption("© 2025 Safebloq. All rights reserved.")
