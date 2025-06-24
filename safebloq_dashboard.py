import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# -------------- Page Config ----------------
st.set_page_config(page_title="Safebloq", layout="wide", initial_sidebar_state="expanded")

# -------------- Theme Toggle ----------------
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

theme_color = "#1F2A44" if st.session_state.dark_mode else "#FFFFFF"
font_color = "#FAFAFA" if st.session_state.dark_mode else "#000000"
bg_color = "#0E1117" if st.session_state.dark_mode else "#F9F9F9"

st.markdown(
    f"""
    <style>
        .reportview-container {{
            background-color: {bg_color};
            color: {font_color};
        }}
        .sidebar .sidebar-content {{
            background-color: {theme_color};
        }}
        .css-18e3th9 {{
            background-color: {bg_color} !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# -------------- Header ----------------
st.markdown(f"<h1 style='color:{font_color};'>Safebloq</h1>", unsafe_allow_html=True)
st.button("Toggle Dark/Light Mode", on_click=toggle_theme)

# -------------- Tab Layout ----------------
tabs = st.tabs(["Overview", "Threats", "Compliance", "Devices", "Team", "Support"])

# -------------- Tab: Overview ----------------
with tabs[0]:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Security Score")
        score_data = {"Score": [85]}
        fig = px.bar(score_data, x=["Security"], y="Score", range_y=[0, 100], text="Score")
        fig.update_layout(height=300, plot_bgcolor=bg_color, paper_bgcolor=bg_color, font_color=font_color)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Live Login Alerts")
        login_data = pd.DataFrame({
            "User": ["jane@company.com", "mike@company.com", "admin@company.com"],
            "Status": ["Success", "Failed", "Failed"],
            "Location": ["London", "Germany", "Nigeria"],
            "Time": [datetime.now().strftime("%H:%M"), "12:44", "11:30"]
        })
        st.dataframe(login_data, use_container_width=True)

# -------------- Tab: Threats ----------------
with tabs[1]:
    st.subheader("Threat Trends (Last 3 Months)")
    threats_df = pd.DataFrame({
        "Month": ["April", "April", "April", "May", "May", "May", "June", "June", "June"],
        "Type": ["Malware", "Phishing", "Unsafe Devices"] * 3,
        "Count": [23, 15, 9, 30, 20, 12, 18, 11, 5]
    })

    threat_chart = px.bar(threats_df, x="Month", y="Count", color="Type", barmode="group",
                          text="Count", height=400)
    threat_chart.update_layout(plot_bgcolor=bg_color, paper_bgcolor=bg_color, font_color=font_color)
    st.plotly_chart(threat_chart, use_container_width=True)

# -------------- Tab: Compliance ----------------
with tabs[2]:
    st.subheader("Reports")
    st.write("- ✅ GDPR Readiness Report")
    st.write("- ✅ Cyber Essentials Checklist")
    st.write("- ✅ Endpoint Encryption Audit")

# -------------- Tab: Devices ----------------
with tabs[3]:
    st.subheader("Device Management")
    st.button("Add New Device")
    st.dataframe(pd.DataFrame({
        "Device": ["Laptop-001", "Mobile-124", "Server-7"],
        "Status": ["Healthy", "Warning", "Unpatched"]
    }))

# -------------- Tab: Team ----------------
with tabs[4]:
    st.subheader("Team Management")
    st.button("Invite Team Member")
    st.dataframe(pd.DataFrame({
        "Name": ["Alice", "Bob", "Eve"],
        "Role": ["Admin", "Analyst", "Viewer"],
        "Status": ["Active", "Pending", "Active"]
    }))

# -------------- Tab: Support ----------------
with tabs[5]:
    st.subheader("Support Center")
    st.markdown("📘 [Support Docs](https://docs.safebloq.com)")
    st.markdown("📘 [User Guide](https://docs.safebloq.com/user-guide)")
    st.markdown("📩 Contact: support@safebloq.com")

# -------------- Footer ----------------
st.markdown(
    "<hr style='border:1px solid #444;'>"
    "<center><small>Safebloq — Cybersecurity for SMBs</small></center>",
    unsafe_allow_html=True
)
