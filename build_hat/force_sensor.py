from time import sleep
from buildhat import ForceSensor

# Initialize the Force Sensor
force_sensor = ForceSensor('B')

print("Force sensor initialized successfully. Monitoring force...")

try:
    while True:
        force = force_sensor.get_force()
        print(f"Current force: {force}N")
        sleep(0.1)  # Adjust the delay to balance responsiveness and resource use
except KeyboardInterrupt:
    print("\nExiting program...")
