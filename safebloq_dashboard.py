import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.patches import Wedge
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# — Streamlit Page Config —

st.set_page_config(
page_title=“Safebloq Dashboard”,
page_icon=“🛡️”,
layout=“wide”,
initial_sidebar_state=“collapsed”
)

# — Custom CSS to match the design —

st.markdown(”””
<style>
.main {
background: linear-gradient(135deg, #87CEEB 0%, #4682B4 100%);
padding: 0;
}

```
    .block-container {
        padding: 1rem;
        max-width: 100%;
    }
    
    /* Header Styling */
    .header {
        background: linear-gradient(135deg, #2C5282 0%, #1A365D 100%);
        padding: 1rem 2rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
    }
    
    .logo {
        display: flex;
        align-items: center;
        font-size: 1.5rem;
        font-weight: bold;
    }
    
    .logo-icon {
        background: white;
        color: #2C5282;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 1rem;
        font-weight: bold;
    }
    
    .user-section {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .user-avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: #4299E1;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
    }
    
    /* Main Content Area */
    .main-content {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .dashboard-title {
        display: flex;
        align-items: center;
        margin-bottom: 2rem;
    }
    
    .dashboard-icon {
        background: #4299E1;
        color: white;
        border-radius: 10px;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 1rem;
        font-size: 1.2rem;
    }
    
    /* Security Score Section */
    .security-score-section {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .security-score-title {
        font-size: 2rem;
        font-weight: bold;
        color: #2D3748;
        margin-bottom: 1rem;
    }
    
    .score-indicators {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-bottom: 2rem;
    }
    
    .score-indicator {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-weight: 600;
    }
    
    .indicator-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
    }
    
    .alert-dot { background-color: #F56565; }
    .soft-dot { background-color: #4299E1; }
    .success-dot { background-color: #48BB78; }
    
    /* Action Buttons */
    .action-buttons {
        position: absolute;
        top: 2rem;
        right: 2rem;
        display: flex;
        gap: 1rem;
    }
    
    .btn {
        padding: 0.75rem 1.5rem;
        border-radius: 10px;
        border: none;
        font-weight: 600;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .btn-primary {
        background: #4299E1;
        color: white;
    }
    
    .btn-secondary {
        background: #E2E8F0;
        color: #4A5568;
    }
    
    /* Cards */
    .card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #E2E8F0;
    }
    
    .card-title {
        font-size: 1.1rem;
        font-weight: bold;
        color: #2D3748;
        margin-bottom: 1rem;
    }
    
    /* Alert Items */
    .alert-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.75rem 0;
        border-bottom: 1px solid #E2E8F0;
    }
    
    .alert-item:last-child {
        border-bottom: none;
    }
    
    .alert-info {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .alert-icon {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
    }
    
    .alert-active { background: #4299E1; }
    .alert-phishing { background: #F6AD55; }
    .alert-unsafe { background: #4299E1; }
    .alert-denial { background: #F56565; }
    .alert-breach { background: #48BB78; }
    
    .alert-count {
        background: #F7FAFC;
        color: #4A5568;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-weight: bold;
    }
    
    /* Support Section */
    .support-item {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 0.75rem 0;
        border-bottom: 1px solid #E2E8F0;
    }
    
    .support-item:last-child {
        border-bottom: none;
    }
    
    .support-icon {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
    }
    
    .support-docs { background: #4299E1; }
    .support-person { background: #4299E1; }
    .support-status { background: #4299E1; }
    
    /* Endpoint Table */
    .endpoint-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem;
        border-bottom: 1px solid #E2E8F0;
    }
    
    .endpoint-item:last-child {
        border-bottom: none;
    }
    
    .endpoint-info {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .endpoint-icon {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
    }
    
    .endpoint-critical { background: #F56565; }
    .endpoint-warning { background: #F6AD55; }
    
    .endpoint-details {
        display: flex;
        flex-direction: column;
    }
    
    .endpoint-name {
        font-weight: bold;
        color: #2D3748;
    }
    
    .endpoint-desc {
        font-size: 0.9rem;
        color: #718096;
    }
    
    .chevron {
        color: #CBD5E0;
        font-size: 1.2rem;
    }
    
    /* Hide Streamlit elements */
    .stDeployButton {
        display: none;
    }
    
    header[data-testid="stHeader"] {
        display: none;
    }
    
    .stMainBlockContainer {
        padding-top: 0;
    }
</style>
```

“””, unsafe_allow_html=True)

def create_security_score_gauge(score=75):
“”“Create a circular gauge for security score”””
fig = go.Figure(go.Indicator(
mode = “gauge+number”,
value = score,
domain = {‘x’: [0, 1], ‘y’: [0, 1]},
title = {‘text’: “”},
gauge = {
‘axis’: {‘range’: [None, 100], ‘tickwidth’: 1, ‘tickcolor’: “darkblue”},
‘bar’: {‘color’: “#2D3748”, ‘thickness’: 0.3},
‘bgcolor’: “white”,
‘borderwidth’: 2,
‘bordercolor’: “gray”,
‘steps’: [
{‘range’: [0, 50], ‘color’: ‘#FED7D7’},
{‘range’: [50, 80], ‘color’: ‘#BEE3F8’},
{‘range’: [80, 100], ‘color’: ‘#C6F6D5’}
],
‘threshold’: {
‘line’: {‘color’: “red”, ‘width’: 4},
‘thickness’: 0.75,
‘value’: 90
}
}
))

```
fig.update_layout(
    height=300,
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)

return fig
```

def create_threat_trends_chart():
“”“Create the threat trends bar chart”””
months = [‘Apr’, ‘May’, ‘Jun’]

```
# Data from the image
user_data = [80, 30, 0]  # User threats
device_data = [30, 60, 75]  # Device threats  
ransomware_data = [30, 45, 85]  # Ransomware threats

fig = go.Figure()

# Add bars for each threat type
fig.add_trace(go.Bar(
    x=months,
    y=user_data,
    name='User',
    marker_color='#4299E1',
    width=0.6
))

fig.add_trace(go.Bar(
    x=months,
    y=device_data,
    name='Device', 
    marker_color='#F56565',
    width=0.6
))

fig.add_trace(go.Bar(
    x=months,
    y=ransomware_data,
    name='Ransomware',
    marker_color='#48BB78',
    width=0.6
))

fig.update_layout(
    height=250,
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    showlegend=False,
    xaxis=dict(
        showgrid=False,
        showline=False,
        zeroline=False
    ),
    yaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='#E2E8F0',
        showline=False,
        zeroline=False,
        range=[0, 100]
    ),
    barmode='group',
    bargap=0.3,
    bargroupgap=0.1
)

return fig
```

def create_live_alerts_chart():
“”“Create the live alerts bar chart”””
months = [‘April’, ‘May’, ‘Jun’, ‘June’]

```
fig = go.Figure()

# Add bars for different alert types
fig.add_trace(go.Bar(
    x=months,
    y=[85, 75, 95, 70],
    name='Active Threats',
    marker_color='#4299E1',
    width=0.6
))

fig.add_trace(go.Bar(
    x=months,
    y=[70, 60, 80, 65],
    name='Phishing Attempts',
    marker_color='#F6AD55',
    width=0.6
))

fig.add_trace(go.Bar(
    x=months,
    y=[60, 50, 70, 55],
    name='Device Breaches',
    marker_color='#F56565',
    width=0.6
))

fig.update_layout(
    height=200,
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    showlegend=False,
    xaxis=dict(
        showgrid=False,
        showline=False,
        zeroline=False
    ),
    yaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='#E2E8F0',
        showline=False,
        zeroline=False
    ),
    barmode='group',
    bargap=0.3,
    bargroupgap=0.1
)

return fig
```

# — Main Dashboard Layout —

# Header

st.markdown(”””
<div class="header">
<div class="logo">
<div class="logo-icon">S</div>
Safebloq
</div>
<div class="user-section">
<span>Quick Actions</span>
<div class="user-avatar">👤</div>
</div>
</div>
“””, unsafe_allow_html=True)

# Main Content Container

st.markdown(’<div class="main-content">’, unsafe_allow_html=True)

# Action Buttons

st.markdown(”””
<div class="action-buttons">
<button class="btn btn-secondary">+ Add Device</button>
<button class="btn btn-primary">Enable MFA</button>
<button class="btn btn-primary">👥 Invite Team</button>
<button class="btn btn-primary">Invite</button>
</div>
“””, unsafe_allow_html=True)

# Dashboard Title

st.markdown(”””
<div class="dashboard-title">
<div class="dashboard-icon">📊</div>
<h1 style="margin: 0; color: #2D3748;">Dashboard</h1>
</div>
“””, unsafe_allow_html=True)

# Security Score Section

st.markdown(”””
<div class="security-score-section">
<div class="security-score-title">Security Score</div>
<div class="score-indicators">
<div class="score-indicator">
<div class="indicator-dot alert-dot"></div>
<span>Alert</span>
</div>
<div class="score-indicator">
<div class="indicator-dot soft-dot"></div>
<span>Soft</span>
</div>
<div class="score-indicator">
<div class="indicator-dot success-dot"></div>
<span>Success</span>
</div>
</div>
</div>
“””, unsafe_allow_html=True)

# Security Score Gauge

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
gauge_fig = create_security_score_gauge(75)
st.plotly_chart(gauge_fig, use_container_width=True)

# Main Content Grid

col1, col2, col3 = st.columns([1, 1, 1])

# Live Alerts Section (Left Column)

with col1:
st.markdown(”””
<div class="card">
<div class="card-title">Live Alerts</div>
<div class="alert-item">
<div class="alert-info">
<div class="alert-icon alert-active">+</div>
<span>Active Threats</span>
</div>
<div class="alert-count">3</div>
</div>
<div class="alert-item">
<div class="alert-info">
<div class="alert-icon alert-phishing">⚠</div>
<span>Phishing Attempts</span>
</div>
<div class="alert-count">5</div>
</div>
<div class="alert-item">
<div class="alert-info">
<div class="alert-icon alert-unsafe">ℹ</div>
<span>Unsafe Devices</span>
</div>
<div class="alert-count">3</div>
</div>
<div class="alert-item">
<div class="alert-info">
<div class="alert-icon alert-denial">⚠</div>
<span>Outbound Denials</span>
</div>
<div class="alert-count">1</div>
</div>
</div>
“””, unsafe_allow_html=True)

```
# Second Live Alerts Card
st.markdown("""
    <div class="card">
        <div class="card-title">Live Alerts</div>
        <div class="alert-item">
            <div class="alert-info">
                <div class="alert-icon alert-active">+</div>
                <span>Active Threats</span>
            </div>
        </div>
        <div class="alert-item">
            <div class="alert-info">
                <div class="alert-icon alert-phishing">⚠</div>
                <span>Phishing Attempts</span>
            </div>
        </div>
        <div class="alert-item">
            <div class="alert-info">
                <div class="alert-icon alert-breach">✓</div>
                <span>Device Breaches</span>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Chart for Live Alerts
live_alerts_fig = create_live_alerts_chart()
st.plotly_chart(live_alerts_fig, use_container_width=True)
```

# Threat Trends Section (Middle Column)

with col2:
st.markdown(”””
<div class="card">
<div class="card-title">Threat Trends</div>
</div>
“””, unsafe_allow_html=True)

```
threat_fig = create_threat_trends_chart()
st.plotly_chart(threat_fig, use_container_width=True)

# Reports Section
st.markdown("""
    <div class="card">
        <div class="card-title">Reports</div>
        <div class="support-item">
            <div class="support-icon support-docs">📄</div>
            <span>Compliance Reports</span>
        </div>
        <div class="support-item">
            <div class="support-icon support-docs">💰</div>
            <span>Savings Calculator</span>
        </div>
    </div>
""", unsafe_allow_html=True)
```

# Right Column - Endpoint Table and Support

with col3:
st.markdown(”””
<div class="card">
<div class="card-title">Endpoint Table</div>
<div class="endpoint-item">
<div class="endpoint-info">
<div class="endpoint-icon endpoint-critical">⚠</div>
<div class="endpoint-details">
<div class="endpoint-name">Red eds</div>
<div class="endpoint-desc">R77 - Inal usen</div>
</div>
</div>
<div class="chevron">›</div>
</div>
<div class="endpoint-item">
<div class="endpoint-info">
<div class="endpoint-icon endpoint-warning">⚠</div>
<div class="endpoint-details">
<div class="endpoint-name">Excessive adim</div>
<div class="endpoint-desc">logons</div>
</div>
</div>
<div class="chevron">›</div>
</div>
</div>
“””, unsafe_allow_html=True)

```
# Support Section
st.markdown("""
    <div class="card">
        <div class="card-title">Support</div>
        <div class="support-item">
            <div class="support-icon support-docs">📚</div>
            <span>Support Docs</span>Ju
            <div class="chevron">›</div>
        </div>
        <div class="support-item">
            <div class="support-icon support-person">👤</div>
            <span>Susan Conn</span>
            <div class="chevron">›</div>
        </div>
        <div class="support-item">
            <div class="support-icon support-status">⚙</div>
            <span>Service Status</span>
            <div class="chevron">›</div>
        </div>
    </div>
""", unsafe_allow_html=True)
```

st.markdown(’</div>’, unsafe_allow_html=True)  # Close main-content
