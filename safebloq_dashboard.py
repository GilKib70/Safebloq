import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ----------------------- Page Config ----------------------- #
st.set_page_config(page_title="Safebloq Dashboard", layout="wide", initial_sidebar_state="expanded")

# ----------------------- Styling --------------------------- #
st.markdown("""
    <style>
        .main { background-color: #0e1117; color: white; }
        .block-container { padding-top: 2rem; }
        .stTabs [role="tab"] {
            background: #1e222d;
            color: white;
            padding: 10px 20px;
            margin: 5px;
            border-radius: 10px;
            border: none;
        }
        .stTabs [role="tab"][aria-selected="true"] {
            background: #3b82f6;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------- Title ----------------------------- #
st.title("Safebloq")

# ----------------------- Security Score -------------------- #
st.subheader("Security Score")
security_score = np.random.randint(40, 100)

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=security_score,
    title={'text': "", 'font': {'size': 24}},
    domain={'x': [0, 1], 'y': [0, 1]},
    gauge={
        'shape': 'semi',
        'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkgray"},
        'bar': {'color': "darkblue"},
        'bgcolor': "#1e1e1e",
        'steps': [
            {'range': [0, 50], 'color': "red"},
            {'range': [50, 80], 'color': "orange"},
            {'range': [80, 100], 'color': "green"}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 0.75,
            'value': security_score}
    }
))

fig.update_layout(
    margin=dict(l=20, r=20, t=30, b=0),
    height=300,
    paper_bgcolor="#0e1117",
    font={'color': "white", 'family': "Arial"},
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------- Live Alerts ----------------------- #
st.subheader("Live Alerts")
alerts = {
    "Active Threats": np.random.randint(0, 10),
    "Phishing Attempts": np.random.randint(0, 5),
    "Outbound Denials": np.random.randint(1, 20),
    "Unsafe Devices": np.random.randint(0, 7)
}
cols = st.columns(len(alerts))
for i, (k, v) in enumerate(alerts.items()):
    with cols[i]:
        st.metric(label=k, value=v)

# ----------------------- Navigation Tabs ------------------- #
tabs = st.tabs(["Devices", "Reports", "Invite Team", "Support"])

# Devices Tab
with tabs[0]:
    st.subheader("Connected Devices")
    device_data = pd.DataFrame({
        "Device": [f"Device {i+1}" for i in range(5)],
        "Status": np.random.choice(["Healthy", "Unsafe"], 5),
        "Last Seen": pd.date_range(end=pd.Timestamp.today(), periods=5).strftime('%Y-%m-%d')
    })
    st.dataframe(device_data)

# Reports Tab
with tabs[1]:
    st.subheader("Compliance Reports")
    report_types = ["GDPR", "Cyber Essentials", "ISO 27001"]
    for rpt in report_types:
        st.markdown(f"**{rpt} Report:** ✅ Available")

# Invite Team Tab
with tabs[2]:
    st.subheader("Invite Team Members")
    email = st.text_input("Enter email address")
    if st.button("Send Invite"):
        st.success(f"Invitation sent to {email}")

# Support Tab
with tabs[3]:
    st.subheader("Support Center")
    st.markdown("### User Docs")
    st.markdown("- [Getting Started](#)")
    st.markdown("- [Dashboard Overview](#)")

    st.markdown("### Support Docs")
    st.markdown("- [Troubleshooting](#)")
    st.markdown("- [Contact Support](#)")
