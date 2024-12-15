import time
import random
import json


# Simulating sensor data
def collect_data():
    data = {
        "vehicle_id": "V123",
        "timestamp": time.time(),
        "location": {
            "latitude": random.uniform(-90, 90),
            "longitude": random.uniform(-180, 180)
        },
        "speed": random.uniform(20, 120),  # km/h
        "hazard": random.choice(["none", "sudden_stop", "road_block"])
    }
    return data


# Test data collection
if __name__ == "__main__":
    while True:
        print(collect_data())
        time.sleep(1)
