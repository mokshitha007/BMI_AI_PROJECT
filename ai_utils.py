import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_ai_response(age, height, weight, bmi, activity, question=None):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"""
                Age: {age}, Height: {height}, Weight: {weight}, BMI: {bmi}, Activity: {activity}
                Question: {question}
                Provide health advice.
                """
            }]
        )
        return response.choices[0].message.content

    except Exception:
        # ✅ FALLBACK (NO FAILURE FOR USERS)
        if bmi < 18.5:
            return "⚠️ AI busy. Basic advice: Increase calorie intake and focus on protein-rich diet."
        elif bmi < 25:
            return "⚠️ AI busy. Basic advice: Maintain balanced diet and regular exercise."
        elif bmi < 30:
            return "⚠️ AI busy. Basic advice: Add cardio and reduce processed foods."
        else:
            return "⚠️ AI busy. Basic advice: Follow structured weight loss plan and consult a professional."