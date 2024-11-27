from microbit import *
import time

# Function to set the servo angle
def set_servo(pin, angle):
    """
    Moves the servo connected to the specified pin to the given angle.
    :param pin: The pin to which the servo is connected (e.g., pin0, pin1, pin2).
    :param angle: The target angle (0 to 180 degrees).
    """
    pulse_width = int(500 + (angle / 180) * 2000)  # Map 0-180° to 500-2500 µs
    pin.write_analog(pulse_width * 1023 // 20000)  # Convert to 0-1023 range
    sleep(20)  # Allow time for the servo to move

# Initialize UART for communication
uart.init(baudrate=115200)

# Debug message to indicate the micro:bit is ready
uart.write("START: Micro:bit ready for servo gate control\n")

# Initialize all servos to the closed position (90 degrees)
set_servo(pin0, 90)
set_servo(pin1, 90)
set_servo(pin2, 90)

# Confirm initialization
uart.write("STATUS: All gates initialized to closed position\n")

# Main loop to listen for commands
while True:
    if uart.any():
        try:
            # Read the incoming command
            command = uart.read().decode('utf-8').strip().upper()

            # Debugging: Log the received command
            uart.write("DEBUG: Received command '{}'\n".format(command))

            # Process the command
            if command == "RED":
                uart.write("ACTION: Opening gate for RED\n")
                set_servo(pin0, 0)  # Open the gate
                sleep(1000)         # Keep the gate open for 1 second
                set_servo(pin0, 90)  # Close the gate
                uart.write("STATUS: Gate for RED closed\n")
            elif command == "BLUE":
                uart.write("ACTION: Opening gate for BLUE\n")
                set_servo(pin1, 0)  # Open the gate
                sleep(1000)         # Keep the gate open for 1 second
                set_servo(pin1, 90)  # Close the gate
                uart.write("STATUS: Gate for BLUE closed\n")
            elif command == "YELLOW":
                uart.write("ACTION: Opening gate for YELLOW\n")
                set_servo(pin2, 0)  # Open the gate
                sleep(1000)         # Keep the gate open for 1 second
                set_servo(pin2, 90)  # Close the gate
                uart.write("STATUS: Gate for YELLOW closed\n")
            else:
                # Unknown command
                uart.write("ERROR: Unknown command '{}'\n".format(command))
        except Exception as e:
            # Handle any unexpected errors
            uart.write("ERROR: {}\n".format(str(e)))

    # Add a small delay to avoid busy-waiting
    sleep(100)
