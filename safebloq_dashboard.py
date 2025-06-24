import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Safebloq Dashboard", layout="wide")

# --- Toggle: Dark Mode ---
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=True)

if dark_mode:
    background_color = "#0e1117"
    text_color = "white"
else:
    background_color = "#f5f7fa"
    text_color = "black"

# Custom styling
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background-color: {background_color};
            color: {text_color};
        }}
        .sidebar .sidebar-content {{
            background-color: #1e1e1e;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header ---
st.markdown(f"<h1 style='color: {text_color};'>🔒 Safebloq Dashboard</h1>", unsafe_allow_html=True)

# --- Columns Layout ---
col1, col2, col3 = st.columns([1.2, 1.5, 1.5])

# --- Live Alerts ---
with col1:
    st.subheader("🚨 Live Alerts")
    st.markdown("🔴 **Active Threats:** 3")
    st.markdown("🟠 **Unpatched Systems:** 3")
    st.markdown("🔵 **Suspicious Logins:** 2")

    st.divider()
    st.subheader("🗂️ Asset Table")
    st.table(pd.DataFrame({
        "Asset Type": ["User", "Device", "Endpoint"],
        "Count": [50, 30, 20]
    }))

# --- Security Score & Compliance ---
with col2:
    st.subheader("🛡️ Security Score")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=82,
        title={'text': "Security"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "green"},
            'steps': [
                {'range': [0, 50], 'color': "red"},
                {'range': [50, 80], 'color': "orange"},
                {'range': [80, 100], 'color': "blue"}
            ]
        }
    ))
    fig.update_layout(height=250, margin=dict(t=0, b=0, l=10, r=10))
    st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.subheader("✅ Compliance Reports")
    st.success("All major compliance reports are up to date.")

# --- Quick Actions & Threats Pie ---
with col3:
    st.subheader("⚙️ Quick Actions")
    st.button("Enable MFA")
    st.button("Invite Team")

    st.divider()
    st.subheader("📊 Threat Dashboard")
    pie_fig = go.Figure(data=[
        go.Pie(labels=["Active Threats", "Phishing Risks", "Breaches"],
               values=[45, 35, 20],
               marker_colors=["#1f77b4", "#00cc96", "red"])
    ])
    pie_fig.update_traces(textinfo='label+percent')
    pie_fig.update_layout(height=300, margin=dict(t=10, b=10, l=10, r=10))
    st.plotly_chart(pie_fig, use_container_width=True)
