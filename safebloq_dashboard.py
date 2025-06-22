import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configure Streamlit page
st.set_page_config(page_title="Safebloq Dashboard", layout="wide")

# Dark Mode Toggle
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=False)

# Apply dark or light styling
if dark_mode:
    st.markdown("""
        <style>
            body { background-color: #1e1e1e; color: #fff; }
            .stApp { background-color: #1e1e1e; color: #fff; }
            .css-18e3th9, .block-container {
                background-color: #2c2c2c !important;
                color: white !important;
                border-radius: 10px;
            }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            body { background-color: #f9fafe; }
            .stApp { background-color: #ffffff; }
            .css-18e3th9, .block-container {
                background-color: #ffffff !important;
                border-radius: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🔐 Safebloq Menu")
page = st.sidebar.radio("Go to", ["Dashboard", "User Access", "Security Controls", "Threat Reports"])

# Expanders for simulated integrations
with st.expander("🔒 Login Status (Simulated)"):
    st.info("✔️ Logged in as: `admin@safebloq.co.uk`")
    st.caption("Authentication via Keycloak will be implemented here.")

with st.expander("🛡️ Ziti Status (Simulated)"):
    st.success("Ziti Overlay: Secure tunnel active.")
    st.caption("Ziti Client SDK integration point.")

# DASHBOARD
if page == "Dashboard":
    st.title("📊 Security Dashboard")

    col1, col2 = st.columns([2, 3])

    # Security score horizontal bar
    with col1:
        score = 82
        st.subheader("Security Score")
        fig1, ax1 = plt.subplots(figsize=(4, 2))
        ax1.barh(0, score, color="#3498db", height=0.4)
        ax1.set_xlim([0, 100])
        ax1.set_yticks([])
        ax1.set_xticks([0, 25, 50, 75, 100])
        ax1.set_title(f"{score}%", fontsize=18, color="#3498db")
        st.pyplot(fig1)

    # Threat trend bar chart
    with col2:
        st.subheader("Threat Trend (Last 3 Months)")
        data = {
            'Threat Type': ['Malware', 'Phishing', 'Device'] * 3,
            'Month': ['April'] * 3 + ['May'] * 3 + ['June'] * 3,
            'Count': [20, 14, 8, 25, 18, 10, 30, 20, 12]
        }
        df = pd.DataFrame(data)
        pivot = df.pivot(index="Threat Type", columns="Month", values="Count")
        fig2, ax2 = plt.subplots(figsize=(6, 3))
        pivot.plot(kind='bar', ax=ax2, colormap='Set2')
        ax2.set_title("Monthly Threat Types")
        ax2.set_ylabel("Threat Count")
        ax2.set_xlabel("Threat Type")
        st.pyplot(fig2)

    # Live alerts
    st.subheader("📍 Live Alerts")
    alerts = [
        ("🔴", "Ransomware detected in finance department"),
        ("🟠", "Suspicious login from unknown IP"),
        ("🟢", "Phishing simulation success: Marketing team")
    ]
    for icon, message in alerts:
        st.write(f"{icon} {message}")

    st.divider()

    # Compliance summary
    st.subheader("📁 Completion Reports")
    st.success("✅ Security controls 85% complete")
    st.info("ℹ️ Compliance template loaded: Cyber Essentials")

# USER ACCESS
elif page == "User Access":
    st.header("👥 Manage User Access")
    st.write("Integration with Keycloak for RBAC. Coming soon.")
    st.button("🔄 Sync Users")

# SECURITY CONTROLS
elif page == "Security Controls":
    st.header("🛠️ Security Controls Overview")
    st.write("Endpoint protection, MFA enforcement, Zero Trust policies.")
    st.progress(85)

# THREAT REPORTS
elif page == "Threat Reports":
    st.header("📈 Monthly Threat Summary")
    st.write("Report downloads and analysis coming soon.")
    st.download_button("⬇️ Download June Report (PDF)", data="Sample Report", file_name="june_report.pdf")
