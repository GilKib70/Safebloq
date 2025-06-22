import streamlit as st
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Safebloq Security Dashboard", layout="wide")

# CSS styling
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title
st.markdown("## 🔐 Safebloq Security Dashboard")

# --- Security Score Pie Chart ---
st.markdown("### Security Score")
fig, ax = plt.subplots()
labels = ['Success', 'Soft', 'Alert']
sizes = [75, 15, 10]
colors = ['#4CAF50', '#FFC107', '#F44336']
ax.pie(sizes, labels=labels, colors=colors, startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'white'})
ax.axis('equal')
st.pyplot(fig)

# --- Live Alerts ---
st.markdown("### 🚨 Live Alerts")
alerts = {
    "Active Threats": 3,
    "Unpatched Systems": 5,
    "Suspicious Logins": 2
}
for key, value in alerts.items():
    st.info(f"{key}: {value}")

# --- Asset Table ---
st.markdown("### 🧱 Asset Table")
st.dataframe({
    'Asset Type': ['User', 'Device', 'Endpoint'],
    'Count': [50, 30, 20],
    'Secure %': [80, 70, 65]
})

# --- Compliance Reports ---
st.markdown("### 📑 Compliance Reports")
st.success("All major compliance reports are up to date.")

# --- Settings & Actions ---
st.markdown("### ⚙️ Quick Actions")
col1, col2 = st.columns(2)
with col1:
    st.button("Enable MFA")
    st.button("Invite Team")
with col2:
    st.button("Run Security Scan")
    st.button("Auto-Fix Issues")
