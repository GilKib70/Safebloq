import streamlit as st
import pandas as pd

# Setup
st.set_page_config(page_title="Safebloq", layout="wide")
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

# Dark mode toggle
def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

dark_mode = st.session_state.theme == "dark"

# Apply theme styling
if dark_mode:
    st.markdown("""
        <style>
            body { background-color: #0e1117; color: white; }
            .card {
                background-color: #1c1e26;
                padding: 1.5rem;
                border-radius: 15px;
                box-shadow: 0 0 10px #00000055;
                margin-bottom: 1rem;
            }
            h1, h2, h3, h4 { color: white !important; }
            .stButton>button { background-color: #3b82f6; color: white; border-radius: 8px; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            .card {
                background-color: #ffffff;
                padding: 1.5rem;
                border-radius: 15px;
                box-shadow: 0 0 10px #00000022;
                margin-bottom: 1rem;
            }
        </style>
    """, unsafe_allow_html=True)

# Header and toggle
st.markdown("<h1 style='text-align: left;'>Safebloq</h1>", unsafe_allow_html=True)
st.button("Toggle Dark/Light Mode", on_click=toggle_theme)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Dashboard", "Devices", "Reports", "Support", "Team"])

# ========== TAB: DASHBOARD ==========
with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.metric("Active Threats", "12", "+3")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.metric("Phishing Attempts", "8", "+1")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.metric("Unsafe Devices", "4", "-1")
        st.markdown('</div>', unsafe_allow_html=True)

    # Threat Trends Graph
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Threat Trend - Last 3 Months")
    df = pd.DataFrame({
        "Month": ["April", "May", "June", "April", "May", "June", "April", "May", "June"],
        "Threat": ["Phishing", "Phishing", "Phishing", "Malware", "Malware", "Malware", "Device Risk", "Device Risk", "Device Risk"],
        "Count": [20, 35, 18, 25, 40, 15, 30, 28, 22]
    })
    chart = df.pivot_table(index="Month", columns="Threat", values="Count", aggfunc="sum")
    st.bar_chart(chart)
    st.markdown('</div>', unsafe_allow_html=True)

    # Live Alerts Table
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Live Login Alerts")
    alert_data = pd.DataFrame({
        "Time": ["12:01", "12:05", "12:15"],
        "User": ["alice@corp", "bob@corp", "carol@corp"],
        "Location": ["UK", "Germany", "India"],
        "Status": ["Blocked", "Allowed", "Blocked"],
        "Threat": ["Brute Force", "Clean", "Phishing"]
    })
    st.dataframe(alert_data)
    st.markdown('</div>', unsafe_allow_html=True)

# ========== TAB: DEVICES ==========
with tab2:
    st.subheader("Connected Devices")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.text("Device list and actions coming soon...")
    st.markdown('</div>', unsafe_allow_html=True)

# ========== TAB: REPORTS ==========
with tab3:
    st.subheader("Compliance Reports")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.text("GDPR, Cyber Essentials, and PCI templates available soon.")
    st.button("Generate New Report")
    st.markdown('</div>', unsafe_allow_html=True)

# ========== TAB: SUPPORT ==========
with tab4:
    st.subheader("Support & Documentation")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("📄 [User Docs](#)\n\n🛠️ [Support Articles](#)")
    st.markdown('</div>', unsafe_allow_html=True)

# ========== TAB: TEAM ==========
with tab5:
    st.subheader("Team Access Management")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.text_input("Invite team member by email")
    st.button("Send Invite")
    st.markdown('</div>', unsafe_allow_html=True)
