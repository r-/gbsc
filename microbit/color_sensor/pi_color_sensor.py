from buildhat import ColorSensor
import serial
import time

# Initialize the color sensor on port C
color_sensor = ColorSensor('C')

# Configure the serial connection to the micro:bit
microbit_port = "/dev/ttyACM0"  # Update if needed
baud_rate = 115200

# Function to identify the color based on RGBI values
def identify_color(rgbi):
    """
    Identifies the color based on custom thresholds.
    :param rgbi: List of [R, G, B, I] values
    :return: Detected color as a string
    """
    r, g, b, intensity = rgbi

    # Ensure valid values
    if r <= 10 and g <= 10 and b <= 10:
        return "None"

    # Custom thresholds for colors
    if r > 50 and g < 50 and b < 40:
        return "RED"
    elif r < 40 and g > 40 and b > 60:
        return "BLUE"
    elif r > 180 and g > 120 and b < 150:
        return "YELLOW"

    return "UNKNOWN"

# Function to send a command to the micro:bit
def send_to_microbit(ser, command):
    """
    Sends a command to the micro:bit.
    :param ser: Serial connection
    :param command: Command to send
    """
    try:
        ser.write((command + "\n").encode('utf-8'))  # Send command
        print(f"Sent to micro:bit: {command}")
        time.sleep(0.1)  # Allow the micro:bit to process
    except Exception as e:
        print(f"Error sending command to micro:bit: {e}")

try:
    # Open the serial connection to the micro:bit
    with serial.Serial(microbit_port, baud_rate, timeout=1) as ser:
        print("Connected to micro:bit.")
        print("Color sensor initialized successfully. Detecting colors...")

        last_sent_time = 0  # Timestamp of the last command sent

        while True:
            rgbi = color_sensor.get_color_rgbi()

            if rgbi:
                color_name = identify_color(rgbi)
                print(f"Detected color: {color_name} (RGBI: {rgbi})")

                current_time = time.time()
                if color_name in ["RED", "BLUE", "YELLOW"]:
                    # Only send command if 3 seconds have passed since the last one
                    if current_time - last_sent_time >= 3:
                        send_to_microbit(ser, color_name)
                        last_sent_time = current_time
                    else:
                        print("Command delayed to prevent spamming.")
                else:
                    print("No actionable color detected.")
            else:
                print("No color detected.")

            time.sleep(0.5)  # Adjust the delay as needed

except serial.SerialException as e:
    print(f"Serial connection error: {e}")
except KeyboardInterrupt:
    print("\nExiting program...")
