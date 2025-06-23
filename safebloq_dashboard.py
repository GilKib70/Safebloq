import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# --- Streamlit Page Config ---
st.set_page_config(page_title="Safebloq Dashboard", layout="wide")

# --- Custom Styles ---
st.markdown("""
    <style>
        .main {
            background-color: #f5faff;
        }
        h1, h2 {
            color: #003366;
        }
        .block-container {
            padding-top: 2rem;
        }
        .card {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        .footer {
            text-align: center;
            font-size: 0.85rem;
            color: #666;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Page Title ---
st.markdown("<h1>🔐 Safebloq Security Dashboard</h1>", unsafe_allow_html=True)
st.markdown("A quick snapshot of your organisation’s security posture and recent threat trends.")

st.markdown("---")

# --- Create Two Columns ---
left_col, right_col = st.columns(2)

# --- Security Score (Left Column) ---
with left_col:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Security Score Overview")

    months = ["April", "May", "June"]
    scores = [72, 80, 88]

    fig1, ax1 = plt.subplots()
    bars = ax1.bar(months, scores, color=['#66b3ff', '#3399ff', '#007acc'])
    ax1.set_ylabel("Security Score (%)")
    ax1.set_ylim(0, 100)
    ax1.set_title("Overall Risk Score")
    ax1.spines[['top','right']].set_visible(False)
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, height - 10, f'{height}%', ha='center', color='white', weight='bold')
    st.pyplot(fig1)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Threat Trends (Right Column) ---
with right_col:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🚨 Threat Trends by Type")

    data = {
        "Month": ["April", "May", "June"],
        "Malware": [12, 9, 6],
        "Phishing": [7, 5, 3],
        "Device Vulnerabilities": [14, 11, 7],
    }

    df = pd.DataFrame(data)

    fig2, ax2 = plt.subplots()
    df.set_index("Month").plot(kind='bar', ax=ax2, colormap="Blues", edgecolor='black')
    ax2.set_ylabel("Threat Events")
    ax2.set_title("Monthly Threat Breakdown")
    ax2.legend(loc='upper right')
    ax2.spines[['top','right']].set_visible(False)
    st.pyplot(fig2)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown('<div class="footer">Built with ❤️ by Safebloq · <a href="https://www.safebloq.co.uk" target="_blank">safebloq.co.uk</a></div>', unsafe_allow_html=True)
