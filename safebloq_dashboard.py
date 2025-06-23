
import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------ Page Config ------------------
st.set_page_config(page_title="Safebloq", layout="wide", initial_sidebar_state="expanded")

# ------------------ Session State ------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ------------------ Login Function ------------------
def login():
    st.markdown("### Login to Safebloq")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")

# ------------------ Sidebar Menu ------------------
def render_sidebar():
    with st.sidebar:
        st.markdown("## 📡 Menu")
        menu = st.radio("Navigation", [
            "Dashboard",
            "Report",
            "Add Device",
            "Invite Team",
            "Support",
        ])

        st.markdown("---")
        st.markdown("#### 👤 Profile")
        st.markdown("**User:** admin")
        st.markdown("**Role:** Administrator")

    return menu

# ------------------ Dashboard Page ------------------
def render_dashboard():
    st.markdown("## Safebloq")

    # ----- Metrics -----
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Threats", "12", "+3 today")
    col2.metric("Phishing Attempts", "7", "+2 today")
    col3.metric("Unsafe Devices", "5", "-1 today")

    col4, col5 = st.columns(2)
    col4.metric("Outbound Denials", "19", "+5 today")
    col5.metric("Security Score", "78%", "-4% since last week")

    # ----- Bar Chart -----
    st.markdown("### Threat Trends (Last 3 Months)")
    data = {
        "Month": ["April", "April", "April", "May", "May", "May", "June", "June", "June"],
        "Threat Type": ["Malware", "Phishing", "Device", "Malware", "Phishing", "Device", "Malware", "Phishing", "Device"],
        "Count": [22, 12, 8, 30, 17, 10, 25, 14, 6]
    }
    df = pd.DataFrame(data)
    fig = px.bar(df, x="Month", y="Count", color="Threat Type", barmode="group",
                 title="Threats by Type Over Last 3 Months", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

# ------------------ Reports Page ------------------
def render_reports():
    st.markdown("## 📄 Compliance Reports")
    st.info("Download compliance reports, audit logs and certificates here. [Coming soon]")

# ------------------ Add Device Page ------------------
def render_add_device():
    st.markdown("## ➕ Add a Device")
    st.success("You can register a device with Wazuh agent. [Feature coming soon]")

# ------------------ Invite Team Page ------------------
def render_invite_team():
    st.markdown("## 👥 Invite Team Members")
    with st.form("invite_form"):
        email = st.text_input("Team member email")
        role = st.selectbox("Assign role", ["Viewer", "Editor", "Admin"])
        submitted = st.form_submit_button("Send Invite")
        if submitted:
            st.success(f"Invitation sent to {email} as {role}")

# ------------------ Support Page ------------------
def render_support():
    st.markdown("## 🛠️ Support Center")
    st.markdown("### 📚 Support Docs")
    st.markdown("- [How to set up your environment](#)")
    st.markdown("- [Wazuh integration guide](#)")
    st.markdown("### 📖 User Docs")
    st.markdown("- [User dashboard walkthrough](#)")
    st.markdown("- [Managing roles and devices](#)")

# ------------------ App Flow ------------------
def main():
    if not st.session_state.logged_in:
        login()
        return

    selected = render_sidebar()

    if selected == "Dashboard":
        render_dashboard()
    elif selected == "Report":
        render_reports()
    elif selected == "Add Device":
        render_add_device()
    elif selected == "Invite Team":
        render_invite_team()
    elif selected == "Support":
        render_support()

# Run the App
if __name__ == "__main__":
    main()
