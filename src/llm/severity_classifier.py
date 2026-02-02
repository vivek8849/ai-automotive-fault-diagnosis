def get_fault_severity(fault_type, engine_temp, engine_rpm):
    if fault_type == "Engine Misfire":
        return "High"
    elif fault_type == "Emission System Fault":
        return "Medium"
    elif fault_type == "Oxygen Sensor Fault":
        return "Low"
    else:
        return "None"