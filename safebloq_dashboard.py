import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="Safebloq Dashboard", layout="wide", initial_sidebar_state="expanded")

# Styling
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .main {
            background-color: #0e1117;
        }
        .css-1d391kg { background-color: #0e1117; }
        .css-ffhzg2 { background-color: #0e1117; }
        .stTabs [role="tab"] {
            background: #1e222d;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 5px;
            border-radius: 10px;
        }
        .stTabs [role="tab"][aria-selected="true"] {
            background: #3b82f6;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Safebloq")

# Simulated Security Score as a Meter Gauge (Semi-Circle)
security_score = np.random.randint(40, 100)

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=security_score,
    title={'text': "Security Score"},
    domain={'x': [0, 1], 'y': [0, 1]},
    gauge={
        'shape': 'semi',
        'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkgray"},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
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

# Fake Alert Summary
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
