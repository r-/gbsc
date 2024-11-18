import explorerhat
import collections
import time

# Rolling average function to smooth pressure readings
def rolling_average(new_value, buffer, size=10):
    """
    Calculate a rolling average of the pressure readings.

    :param new_value: The latest pressure reading.
    :param buffer: A deque storing previous readings.
    :param size: The number of readings to average over.
    :return: The smoothed pressure value.
    """
    buffer.append(new_value)
    if len(buffer) > size:
        buffer.popleft()
    return sum(buffer) / len(buffer)

# Function to read and convert analog voltage to pressure
def read_pressure():
    """
    Reads voltage from the analog input and converts it to pressure.

    :return: Pressure in kPa.
    """
    # Read voltage from analog input 1
    voltage = explorerhat.analog.one.read()
    
    # Convert voltage to pressure (kPa) using the sensor formula
    pressure = ((voltage - 0.1) / 3.0) * 300.0 - 100.0
    
    return pressure

# Main loop
def main():
    """
    Main loop to continuously read and display smoothed pressure readings.
    """
    readings_buffer = collections.deque()  # Buffer for rolling average
    
    try:
        print("Reading pressure. Press Ctrl+C to exit.")
        while True:
            pressure = read_pressure()
            smoothed_pressure = rolling_average(pressure, readings_buffer)
            print(f"Smoothed Pressure: {smoothed_pressure:.2f} kPa")
            time.sleep(1)  # Delay for 1 second
    except KeyboardInterrupt:
        print("\nProgram terminated.")

# Run the main loop
if __name__ == "__main__":
    main()
