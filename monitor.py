def check_readings(voltage, current, temperature):
    alerts = []

    if voltage < 210 or voltage > 250:
        alerts.append("Voltage is outside the configured range")

    if current < 0 or current > 10:
        alerts.append("Current is outside the configured range")

    if temperature < 0 or temperature > 70:
        alerts.append("Temperature is outside the configured range")

    if alerts:
        return alerts

    return ["All readings are within the configured limits"]


reading = {
    "voltage": 230,
    "current": 5,
    "temperature": 85
}

results = check_readings(
    reading["voltage"],
    reading["current"],
    reading["temperature"]
)

for result in results:
    print(result)