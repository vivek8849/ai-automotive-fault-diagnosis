from fastapi import FastAPI
import pickle
import os
import sys

# Fix imports
sys.path.append(os.path.abspath("."))

from src.api.schemas import VehicleInput, PredictionResponse
from src.llm.severity_classifier import get_fault_severity
from src.llm.prompt_templates import fault_explanation_prompt
from src.llm.explanation_engine import generate_explanation

app = FastAPI(title="AI Automotive Fault Diagnosis API")

# Load ML model & encoder
with open("models/fault_classifier.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)


@app.get("/")
def health_check():
    return {"status": "API is running"}


@app.post("/predict", response_model=PredictionResponse)
def predict_fault(data: VehicleInput):
    features = [[
        data.engine_rpm,
        data.vehicle_speed,
        data.engine_temp,
        data.intake_pressure
    ]]

    # ML prediction
    prediction_encoded = model.predict(features)[0]
    fault = label_encoder.inverse_transform([prediction_encoded])[0]

    # Severity logic
    severity = get_fault_severity(
        fault,
        data.engine_temp,
        data.engine_rpm
    )

    # LLM explanation
    sensor_summary = f"""
    Engine RPM: {data.engine_rpm}
    Vehicle Speed: {data.vehicle_speed}
    Engine Temperature: {data.engine_temp}
    Intake Pressure: {data.intake_pressure}
    """

    prompt = fault_explanation_prompt(fault, severity, sensor_summary)
    explanation = generate_explanation(prompt)

    return {
        "fault": fault,
        "severity": severity,
        "explanation": explanation
    }