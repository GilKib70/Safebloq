import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dummy credentials (for demo only)
USERNAME = "admin"
PASSWORD = "safebloq123"

# Page config
st.set_page_config(page_title="Safebloq", layout="wide", page_icon="🔐")

# Session state to track login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ------------------------
# Login Page
# ------------------------
def login():
    st.title("Safebloq")

    st.markdown("## 🔐 Login to continue")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password.")

# ------------------------
# Sidebar Navigation
# ------------------------
def sidebar():
    menu = st.sidebar.selectbox("📁 Menu", ["Dashboard", "Assets", "Alerts", "Logout"])
    return menu

# ------------------------
# Dashboard Page
# ------------------------
def dashboard():
    st.title("Safebloq")

    # Security Score
    st.markdown("### 🔵 Security Score")
    st.progress(0.72)

    # Endpoint Protection
    st.markdown("### 🖥️ Endpoint Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Protected Devices", "43", "+5")
    col2.metric("Unprotected Devices", "7", "-2")
    col3.metric("Devices Needing Attention", "3", "⚠")

    # Threat Bar Chart (3 months)
    st.markdown("### 📊 Threats Over Last 3 Months")
    threat_data = pd.DataFrame({
        "Month": ["April", "May", "June"],
        "Malware": [12, 8, 15],
        "Phishing": [5, 7, 6],
        "Device Attacks": [3, 2, 4]
    })
    fig, ax = plt.subplots(figsize=(8, 4))
    bar_width = 0.2
    months = range(len(threat_data["Month"]))
    ax.bar([m - bar_width for m in months], threat_data["Malware"], width=bar_width, label="Malware")
    ax.bar(months, threat_data["Phishing"], width=bar_width, label="Phishing")
    ax.bar([m + bar_width for m in months], threat_data["Device Attacks"], width=bar_width, label="Device Attacks")
    ax.set_xticks(months)
    ax.set_xticklabels(threat_data["Month"])
    ax.set_ylabel("Incidents")
    ax.set_title("Monthly Threat Categories")
    ax.legend()
    st.pyplot(fig)

# ------------------------
# Assets Page
# ------------------------
def assets():
    st.title("Safebloq")
    st.markdown("### 📋 Asset Overview")
    asset_data = pd.DataFrame({
        "Asset": ["Laptop-001", "Desktop-023", "Mobile-112", "Tablet-019"],
        "Status": ["Protected", "Needs Update", "Protected", "Unprotected"],
        "Last Checked": ["Today", "Yesterday", "Today", "2 days ago"]
    })
    st.dataframe(asset_data)

# ------------------------
# Alerts Page
# ------------------------
def alerts():
    st.title("Safebloq")
    st.markdown("### 🚨 Security Alerts")
    alerts = [
        {"time": "10:21 AM", "alert": "Phishing attempt blocked on user device"},
        {"time": "9:10 AM", "alert": "Outdated software on workstation #22"},
        {"time": "Yesterday", "alert": "Ransomware blocked from suspicious IP"},
    ]
    for alert in alerts:
        st.info(f"[{alert['time']}] {alert['alert']}")

# ------------------------
# Main App
# ------------------------
def main():
    if not st.session_state.logged_in:
        login()
    else:
        page = sidebar()

        if page == "Dashboard":
            dashboard()
        elif page == "Assets":
            assets()
        elif page == "Alerts":
            alerts()
        elif page == "Logout":
            st.session_state.logged_in = False

main()
