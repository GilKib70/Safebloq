import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Page config
st.set_page_config(page_title="Safebloq Security Dashboard", layout="wide")

# Custom CSS for blue-white theme
st.markdown("""
    <style>
        body {
            background-color: #f0f8ff;
        }
        .main {
            background-color: #f0f8ff;
        }
        .block-container {
            padding-top: 2rem;
        }
        h1 {
            color: #003366;
            font-size: 2.5em;
            margin-bottom: 0.5em;
        }
        .card {
            background-color: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Dashboard Header
st.markdown("<h1>Safebloq Security Dashboard</h1>", unsafe_allow_html=True)

# Section: Security Score + Threats Bar Chart
with st.container():
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("<div class='card'><h3 style='color:#003366;'>Your Security Score</h3>", unsafe_allow_html=True)
        st.progress(0.82)
        st.markdown("<p style='font-size: 18px;'>Overall Security Rating: 82%</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'><h3 style='color:#003366;'>Threat Types Over Last 3 Months</h3>", unsafe_allow_html=True)

        # Sample data
        data = {
            'Month': ['April', 'May', 'June'],
            'Malware': [5, 7, 3],
            'Phishing': [2, 4, 6],
            'Device Threats': [3, 5, 2]
        }
        df = pd.DataFrame(data)

        # Plot chart
        fig, ax = plt.subplots(figsize=(6, 4))
        df.set_index('Month').plot(kind='bar', stacked=True, ax=ax,
                                   color=['#003366', '#007acc', '#66c2ff'])
        ax.set_ylabel("Number of Threats")
        ax.set_title("Threat Breakdown by Month")
        ax.legend(title="Threat Type", bbox_to_anchor=(1.05, 1), loc='upper left')
        st.pyplot(fig)

        st.markdown("</div>", unsafe_allow_html=True)
