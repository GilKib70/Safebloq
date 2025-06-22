import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Custom page config and background
st.set_page_config(page_title="Safebloq MVP", layout="wide")

# Inject background color (white + soft blue)
st.markdown("""
    <style>
        body {
            background: linear-gradient(to bottom right, #ffffff, #e6f0ff);
        }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ Safebloq - Zero Trust Cybersecurity for SMBs")
st.markdown("A simple dashboard MVP showcasing real-time security visibility for small businesses.")

# --- Security Events Table ---
st.header("🚨 Detected Security Events")
data = {
    "Time": ["09:01", "09:14", "09:26", "10:05"],
    "Event Type": ["Phishing Attempt", "Suspicious Login", "Ransomware Blocked", "USB Access Denied"],
    "Device": ["Laptop-01", "Mobile-Admin", "Desktop-Accounting", "Tablet-Warehouse"],
    "Status": ["Blocked", "Alert", "Quarantined", "Blocked"]
}
df = pd.DataFrame(data)
st.dataframe(df)

# --- Incident Overview Chart ---
st.header("📊 Incident Overview")
chart_data = pd.DataFrame({
    "Blocked": [12, 18, 24, 30],
    "Quarantined": [5, 6, 4, 8],
    "Alerts": [3, 4, 5, 7]
}, index=["Mon", "Tue", "Wed", "Thu"])
st.bar_chart(chart_data)

# --- Security Health Metrics ---
st.header("✅ Security Health")
col1, col2, col3 = st.columns(3)
col1.metric("Devices Secured", "56", "+6")
col2.metric("Threats Blocked", "102", "+12")
col3.metric("Users Protected", "43", "+3")

# --- Security Score Pie Chart ---
st.header("🔒 Security Score Breakdown")

labels = ['Protection', 'Response', 'Detection', 'Compliance']
sizes = [35, 25, 25, 15]
colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728']

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax1.axis('equal')
st.pyplot(fig1)

st.info("This MVP demo shows simulated activity. Real-time integration will occur in beta release.")
