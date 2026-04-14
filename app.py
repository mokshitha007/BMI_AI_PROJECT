import streamlit as st
import pandas as pd
from datetime import datetime
from ai_utils import generate_ai_response
from components import calculate_bmi, get_bmi_category, calculate_health_score

# Page Config
st.set_page_config(page_title="AI Health Advisor", layout="wide")

#debug line
st.write(st.secrets)

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Session State
if "history" not in st.session_state:
    st.session_state.history = []

st.title("🧠 AI Health Advisor")
st.caption("Data-driven health insights powered by AI")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Input Your Data")
    age = st.slider("Age", 10, 80)
    height = st.number_input("Height (cm)", 100.0, 250.0)
    weight = st.number_input("Weight (kg)", 20.0, 200.0)
    activity = st.selectbox("Activity Level", ["Low", "Moderate", "High"])

    analyze = st.button("🔍 Analyze")

with col2:
    if analyze:
        bmi = calculate_bmi(height, weight)
        st.session_state.bmi=bmi

        #debug here
        st.write("Stored BMI:",st.session_state.get("bmi"))
        category = get_bmi_category(bmi)
        score = calculate_health_score(bmi, activity)

        st.metric("BMI", f"{bmi:.2f}")
        st.metric("Health Score", f"{score}/100")
        st.write(f"### Category: {category}")

        # Save history
        st.session_state.history.append({
            "Time": datetime.now(),
            "BMI": bmi,
            "Weight": weight
        })

        # AI Insight
        with st.spinner("Generating AI insights..."):
            response = generate_ai_response(age, height, weight, bmi, activity)

        st.write("### 🧠 AI Insight")
        st.write(response)

# History Section
if st.session_state.history:
    st.write("## 📊 Progress Tracker")
    df = pd.DataFrame(st.session_state.history)
    st.line_chart(df.set_index("Time")["BMI"])

# AI Chat
st.write("## 💬 AI Health Chat")

user_query = st.text_input("Ask anything about your health:")

if st.button("Ask AI"):
    if user_query:
        reply = generate_ai_response(age, height, weight, st.session_state.bmi, activity, user_query)
        st.write(reply)