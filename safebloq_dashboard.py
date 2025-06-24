import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Set page config
st.set_page_config(page_title="Safebloq", layout="wide")

# Apply dark mode styling
st.markdown("""
    <style>
        body {
            background-color: #0d1b2a;
            color: white;
        }
        .block-container {
            padding-top: 2rem;
        }
        .css-1d391kg {background-color: #1b263b;}
        .stButton>button {
            background-color: #1c74d9;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
col1, col2 = st.columns([8, 2])
with col1:
    st.markdown("## <span style='color:white;'>Safebloq</span>", unsafe_allow_html=True)
with col2:
    st.markdown("#### 👤 Quick Actions")

st.markdown("---")

# --- SECURITY SCORE ---
st.markdown("### 🔐 Security Score")
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=75,
    domain={'x': [0, 1], 'y': [0, 1]},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "darkblue"},
        'steps': [
            {'range': [0, 50], 'color': "red"},
            {'range': [50, 75], 'color': "orange"},
            {'range': [75, 100], 'color': "lightblue"}
        ],
    },
    number={'suffix': "%"}
))
st.plotly_chart(fig, use_container_width=True)

# --- LIVE ALERTS ---
st.markdown("### 🚨 Live Alerts")
alerts = {
    "Active Threats": 3,
    "Phishing Attempts": 5,
    "Unsafe Devices": 3,
    "Outbound Denials": 1
}
alert_cols = st.columns(len(alerts))
for i, (alert, count) in enumerate(alerts.items()):
    alert_cols[i].metric(label=alert, value=count)

# --- THREAT TRENDS ---
st.markdown("### 📊 Threat Trends (April - June)")
trend_data = {
    "Month": ["April", "May", "June"],
    "User": [80, 65, 30],
    "Device": [30, 50, 60],
    "Ransomware": [20, 25, 45]
}
df = pd.DataFrame(trend_data)
fig_bar = go.Figure()
fig_bar.add_trace(go.Bar(name='User', x=df["Month"], y=df["User"]))
fig_bar.add_trace(go.Bar(name='Device', x=df["Month"], y=df["Device"]))
fig_bar.add_trace(go.Bar(name='Ransomware', x=df["Month"], y=df["Ransomware"]))
fig_bar.update_layout(barmode='group', plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_bar, use_container_width=True)

# --- ENDPOINT TABLE ---
st.markdown("### 🖥️ Endpoint Table")
endpoint_data = {
    "Alert": ["Red eds", "Excessive admin logons"],
    "Details": ["R77 – Invalid users", "Multiple failed logons"]
}
st.table(pd.DataFrame(endpoint_data))

# --- REPORTS ---
st.markdown("### 📁 Reports")
st.button("📋 Compliance Reports")
st.button("💰 Savings Calculator")

# --- SUPPORT SECTION ---
st.markdown("### 🛠️ Support")
support_cols = st.columns(3)
support_cols[0].button("📖 Support Docs")
support_cols[1].button("👩 Susan Conn")
support_cols[2].button("📡 Service Status")
