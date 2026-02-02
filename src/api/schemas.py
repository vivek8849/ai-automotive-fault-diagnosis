from pydantic import BaseModel

class VehicleInput(BaseModel):
    engine_rpm: int
    vehicle_speed: int
    engine_temp: int
    intake_pressure: int


class PredictionResponse(BaseModel):
    fault: str
    severity: str
    explanation: str