import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Safebloq", layout="wide")
st.markdown("""
    <style>
        body {background-color: #f0f6ff;}
        .main {background-color: #ffffff; padding: 2rem; border-radius: 10px;}
        h1, h2, h3, h4 {color: #114B8A;}
        .css-1d391kg {background-color: #f0f6ff;}
        .block-container {padding-top: 2rem;}
    </style>
""", unsafe_allow_html=True)

# Mock login
def login():
    st.markdown("<h1>Safebloq</h1>", unsafe_allow_html=True)
    st.markdown("## Login to access your security dashboard")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")

# Sample threat data
def get_threat_data():
    return pd.DataFrame({
        "Month": ["April", "May", "June"],
        "Malware": [25, 30, 22],
        "Phishing": [18, 25, 20],
        "Device Intrusion": [10, 14, 12],
        "Policy Violations": [5, 8, 6]
    })

# Sample login alerts
def get_login_alerts():
    return pd.DataFrame({
        "Timestamp": ["2025-06-20 10:15", "2025-06-21 13:45", "2025-06-22 09:00", "2025-06-23 11:30"],
        "Username": ["user1", "user2", "user3", "admin"],
        "Source IP": ["192.168.1.5", "172.16.0.3", "10.0.0.2", "192.168.1.10"],
        "Outcome": ["Success", "Failed", "Success", "Failed"]
    })

# Dashboard
def main_dashboard():
    st.markdown("<h1>Safebloq</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 3])

    with col1:
        st.subheader("Security Score")
        score = 78
        st.progress(score / 100)
        st.metric(label="Security Health", value=f"{score}%", delta="+6%")

    with col2:
        st.subheader("Threat Trends (Last 3 Months)")
        df = get_threat_data()
        df.set_index("Month", inplace=True)
        df.plot(kind="bar", figsize=(10, 4), colormap="Blues")
        st.pyplot(plt)

    st.markdown("---")
    st.subheader("Live Login Alerts (Simulated)")
    st.dataframe(get_login_alerts(), use_container_width=True)

# App init
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    main_dashboard()
else:
    login()
