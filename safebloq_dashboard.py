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
    st.title("🔐 Safebloq Secure Login")
    st.subheader("Zero Trust Cybersecurity for SMBs")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            if username == USERNAME and password == PASSWORD:
                st.session_state.logged_in = True
                st.success("Login successful")
                st.experimental_rerun()
            else:
                st.error("Invalid credentials")

# ------------------------
# Sidebar Navigation
# ------------------------
def sidebar():
    menu = st.sidebar.selectbox("📁 Navigate", ["Dashboard", "Assets", "Alerts", "Logout"])
    return menu

# ------------------------
# Dashboard Page
# ------------------------
def dashboard():
    st.title("Safebloq")
    st.subheader("Zero Trust for SMBs – Secure Everything, Everywhere")

    # Security Score
    st.markdown("### 🔵 Overall Security Score")
    st.progress(0.72)

    # Endpoint Status Section
    st.markdown("### 🖥️ Endpoint Protection Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Protected Devices", "43", "+5")
    col2.metric("Unprotected Devices", "7", "-2")
    col3.metric("Devices Needing Attention", "3", "⚠")

    # Threat Bar Chart
    st.markdown("### 📊 Threat Trends (Last 3 Months)")
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
    ax.set_title("Threat Categories by Month")
    ax.legend()
    st.pyplot(fig)

# ------------------------
# Assets Page
# ------------------------
def assets():
    st.title("📋 Asset Protection Summary")
    asset_data = pd.DataFrame({
        "Asset Name": ["Laptop-001", "Desktop-023", "Mobile-112", "Tablet-019"],
        "Status": ["Protected", "Needs Update", "Protected", "Unprotected"],
        "Last Checked": ["Today", "Yesterday", "Today", "2 days ago"]
    })
    st.dataframe(asset_data)

# ------------------------
# Alerts Page
# ------------------------
def alerts():
    st.title("🚨 Live Security Alerts")
    alerts = [
        {"time": "10:21 AM", "alert": "New phishing attempt blocked on user device"},
        {"time": "9:10 AM", "alert": "Outdated software detected on workstation #22"},
        {"time": "Yesterday", "alert": "Ransomware attempt blocked from suspicious IP"},
    ]
    for alert in alerts:
        st.info(f"[{alert['time']}] {alert['alert']}")

# ------------------------
# Main App Logic
# ------------------------
def main():
    if not st.session_state.logged_in:
        login()
    else:
        choice = sidebar()

        if choice == "Dashboard":
            dashboard()
        elif choice == "Assets":
            assets()
        elif choice == "Alerts":
            alerts()
        elif choice == "Logout":
            st.session_state.logged_in = False
            st.experimental_rerun()

main()
