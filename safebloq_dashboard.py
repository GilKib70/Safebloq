import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# --- MOCK: Replace this function later with Wazuh API call ---
def get_mock_login_alerts():
    return pd.DataFrame({
        "User": ["jane.doe", "john.smith", "admin", "emily.wu", "mark.ray"],
        "IP Address": ["192.168.1.10", "192.168.1.15", "203.0.113.2", "10.0.0.25", "172.16.4.5"],
        "Login Time": ["08:45", "09:20", "03:15", "10:02", "11:47"],
        "Status": ["Failed", "Success", "Failed", "Success", "Failed"]
    })

# --- LOGIN ---
def login():
    st.markdown("<h1 style='text-align: center; color: white;'>Safebloq</h1>", unsafe_allow_html=True)
    st.markdown("## Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username and password:
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Please enter both fields.")

# --- SIDEBAR ---
def sidebar_menu():
    menu = ["Dashboard", "Settings", "Logout"]
    choice = st.sidebar.radio("Menu", menu)
    if choice == "Logout":
        st.session_state.logged_in = False
        st.experimental_rerun()
    return choice

# --- THREAT CHART ---
def show_threat_chart():
    st.subheader("📊 Threat Trends (Last 3 Months)")
    months = ["April", "May", "June"]
    threat_data = {
        "Month": months * 3,
        "Threat Type": ["Malware"] * 3 + ["Phishing"] * 3 + ["Device"] * 3,
        "Incidents": [23, 18, 30, 12, 15, 20, 7, 11, 13]
    }
    df = pd.DataFrame(threat_data)
    plt.figure(figsize=(8, 4))
    sns.barplot(data=df, x="Month", y="Incidents", hue="Threat Type")
    plt.title("Threat Incidents by Type")
    plt.tight_layout()
    st.pyplot(plt)

# --- LOGIN ALERT TABLE ---
def show_live_login_alerts():
    st.subheader("🔔 Live Login Alerts (from Wazuh)")
    df = get_mock_login_alerts()
    def highlight_status(val):
        color = "red" if val == "Failed" else "green"
        return f"color: {color}; font-weight: bold;"
    st.dataframe(df.style.applymap(highlight_status, subset=["Status"]), use_container_width=True)

# --- MAIN DASHBOARD ---
def show_dashboard():
    st.markdown("<h2 style='color:#003366;'>Safebloq Security Dashboard</h2>", unsafe_allow_html=True)
    st.markdown("---")
    show_threat_chart()
    st.markdown("---")
    show_live_login_alerts()

# --- MAIN APP ---
def main():
    st.set_page_config(page_title="Safebloq", layout="wide", page_icon="🔐")

    # Background color styling
    st.markdown("""
        <style>
        body {background-color: #f0f8ff;}
        .stApp {background-color: #e6f2ff;}
        </style>
    """, unsafe_allow_html=True)

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        login()
    else:
        page = sidebar_menu()
        if page == "Dashboard":
            show_dashboard()
        elif page == "Settings":
            st.write("🔧 Settings (Coming Soon)")

if __name__ == "__main__":
    main()
