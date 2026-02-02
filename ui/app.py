import streamlit as st
import requests

st.set_page_config(page_title="AI Automotive Fault Diagnosis", layout="centered")

st.title("🚗 AI Automotive Fault Diagnosis System")
st.write("Enter vehicle sensor values to diagnose potential faults.")

# Input fields
engine_rpm = st.number_input("Engine RPM", min_value=0, value=1500)
vehicle_speed = st.number_input("Vehicle Speed (km/h)", min_value=0, value=60)
engine_temp = st.number_input("Engine Temperature (°C)", min_value=0, value=90)
intake_pressure = st.number_input("Intake Pressure", min_value=0, value=40)

if st.button("🔍 Diagnose Vehicle"):
    payload = {
        "engine_rpm": engine_rpm,
        "vehicle_speed": vehicle_speed,
        "engine_temp": engine_temp,
        "intake_pressure": intake_pressure
    }

    try:
        response = requests.post(
        "http://api:8000/predict",
        json=payload
    )   

        if response.status_code == 200:
            result = response.json()

            st.success(f"🛠️ Fault Detected: {result['fault']}")
            st.warning(f"⚠️ Severity Level: {result['severity']}")
            st.subheader("🧠 AI Explanation")
            st.markdown(f"```\n{result['explanation']}\n```")

        else:
            st.error("Error communicating with the API")

    except Exception as e:
        st.error(f"Connection error: {e}")