import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Safebloq", layout="wide")

# -------- Custom Dark Theme Styling --------
st.markdown("""
    <style>
        body, .stApp {
            background-color: #0c1c2c;
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }
        .block-container {
            padding: 1rem 2rem;
        }
        .title {
            font-size: 2rem;
            font-weight: bold;
            color: #4DB8FF;
        }
        .card {
            background-color: #14273a;
            border-radius: 10px;
            padding: 1.2rem;
            margin-bottom: 1.2rem;
        }
        .metric-label {
            color: #B0BEC5;
            font-size: 0.85rem;
        }
        .metric-value {
            font-size: 1.5rem;
            font-weight: bold;
            color: #ffffff;
        }
        .tab-style {
            background-color: #0f263a;
            padding: 1rem;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# -------- Navigation Tabs --------
tabs = st.tabs(["Dashboard", "Devices", "Live Alerts", "Compliance", "Support", "Team"])

# --------- Tab 1: Dashboard ---------
with tabs[0]:
    st.markdown('<div class="title">Safebloq Security Dashboard</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card"><div class="metric-label">Security Score</div><div class="metric-value">82%</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><div class="metric-label">Devices Online</div><div class="metric-value">145</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card"><div class="metric-label">Active Users</div><div class="metric-value">197</div></div>', unsafe_allow_html=True)

    # Threat Trends Bar Graph
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Threat Trend - Last 3 Months")

    df = pd.DataFrame({
        "Month": ["April", "May", "June"] * 3,
        "Threat": ["Phishing", "Malware", "Device Risk"] * 3,
        "Count": [20, 35, 18, 25, 40, 15, 30, 28, 22]
    })

    chart = df.pivot(index="Month", columns="Threat", values="Count")
    st.bar_chart(chart)
    st.markdown('</div>', unsafe_allow_html=True)

# --------- Tab 2: Devices ---------
with tabs[1]:
    st.markdown('<div class="title">Managed Devices</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">145 devices active. Endpoint data coming soon.</div>', unsafe_allow_html=True)

# --------- Tab 3: Live Alerts ---------
with tabs[2]:
    st.markdown('<div class="title">Live Threat Alerts</div>', unsafe_allow_html=True)

    # Mock Alert Table
    alerts = pd.DataFrame([
        {"Time": "10:12", "Type": "Phishing", "Severity": "High", "Device": "HR-PC-22"},
        {"Time": "09:58", "Type": "Malware", "Severity": "Medium", "Device": "Sales-LT-03"},
        {"Time": "09:41", "Type": "Unsafe App", "Severity": "Low", "Device": "Dev-Mac-11"},
    ])
    st.dataframe(alerts, use_container_width=True)

# --------- Tab 4: Compliance ---------
with tabs[3]:
    st.markdown('<div class="title">Compliance Reports</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">GDPR and Cyber Essentials reports coming soon. Export button to be added.</div>', unsafe_allow_html=True)

# --------- Tab 5: Support ---------
with tabs[4]:
    st.markdown('<div class="title">Support Centre</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">Access our <a href="#">Support Docs</a> and <a href="#">User Manual</a>.</div>', unsafe_allow_html=True)

# --------- Tab 6: Team ---------
with tabs[5]:
    st.markdown('<div class="title">Team & Access Control</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">Invite new team members and assign access levels here.</div>', unsafe_allow_html=True)
