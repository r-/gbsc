from buildhat import DistanceSensor
from time import sleep

# Initialize the Distance Sensor on port C
distance_sensor = DistanceSensor('C')

print("Distance sensor initialized successfully. Reading distances...")

try:
    while True:
        distance = distance_sensor.get_distance()
        if distance is not None:
            print(f"Distance: {distance} mm")
        else:
            print("No object detected.")
        sleep(0.5)  # Adjust the delay as needed
except KeyboardInterrupt:
    print("\nExiting program...")
