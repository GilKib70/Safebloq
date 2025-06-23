import streamlit as st
import pandas as pd
import plotly.express as px

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# -----------------------
# Login Function
# -----------------------
def login():
    st.markdown("<h1 style='text-align: center; color: #1f77b4;'>Safebloq</h1>", unsafe_allow_html=True)
    st.subheader("Login")

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            if username == "admin" and password == "admin":
                st.session_state.logged_in = True
                st.success("Login successful")
                st.stop()  # Prevent error
            else:
                st.error("Invalid credentials")

# -----------------------
# Sample Threat Trend Data (3 months x 4 threats)
# -----------------------
def get_threat_trend_data():
    data = {
        "Month": ["April", "April", "April", "April",
                  "May", "May", "May", "May",
                  "June", "June", "June", "June"],
        "Threat Type": ["Malware", "Phishing", "Device", "Ransomware"] * 3,
        "Count": [15, 8, 12, 4, 10, 14, 7, 3, 18, 10, 6, 5]
    }
    return pd.DataFrame(data)

# -----------------------
# Sample Login Alerts Table
# -----------------------
def get_login_alert_data():
    data = {
        "Time": ["2025-06-22 08:32", "2025-06-22 09:05", "2025-06-22 09:33"],
        "User": ["alice@company.com", "bob@company.com", "eve@company.com"],
        "Location": ["UK", "US", "RU"],
        "Status": ["Success", "Failed", "Failed"],
        "Alert Level": ["Low", "High", "Critical"]
    }
    return pd.DataFrame(data)

# -----------------------
# Main Dashboard
# -----------------------
def dashboard():
    st.markdown("""
        <style>
            .main {
                background-color: #f0f8ff;
                padding: 20px;
            }
            .stApp {
                background-color: #f0f8ff;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='color: #1f77b4;'>Safebloq Security Dashboard</h1>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Threat Trends (Last 3 Months)")
    threat_df = get_threat_trend_data()

    chart = px.bar(
        threat_df,
        x="Month",
        y="Count",
        color="Threat Type",
        barmode="group",
        title="Threat Events by Type",
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    st.plotly_chart(chart, use_container_width=True)

    st.markdown("---")
    st.subheader("Live Login Alerts")
    alert_df = get_login_alert_data()
    st.dataframe(alert_df, use_container_width=True)

# -----------------------
# Main App
# -----------------------
def main():
    if not st.session_state.logged_in:
        login()
    else:
        dashboard()

if __name__ == "__main__":
    main()
