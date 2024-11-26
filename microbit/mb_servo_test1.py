from microbit import *
import time

# Function to set the servo angle
def set_servo(pin, angle):
    pulse_width = int(500 + (angle / 180) * 2000)  # Map 0-180° to 500-2500 µs
    pin.write_analog(pulse_width * 1023 // 20000)  # Convert to 0-1023 range
    time.sleep(0.02)  # Delay to let the servo move

# Initialize UART for communication
uart.init(baudrate=115200)

# **INITIALIZATION**: Set all servos to 90 degrees (neutral position)
set_servo(pin0, 90)
set_servo(pin1, 90)
set_servo(pin2, 90)

# Confirm initialization via UART
uart.write("Servos initialized to 90 degrees\n")

# Main loop for receiving commands
while True:
    if uart.any():
        try:
            # Read the incoming command and clean it up
            command = uart.read().decode('utf-8').strip().upper()
            
            # Parse the command (e.g., "P0 90")
            parts = command.split()
            if len(parts) == 2:
                pin_id, angle = parts[0], int(parts[1])
                if pin_id == "P0":
                    set_servo(pin0, angle)
                    uart.write("OK: Set P0 to " + str(angle) + "\n")
                elif pin_id == "P1":
                    set_servo(pin1, angle)
                    uart.write("OK: Set P1 to " + str(angle) + "\n")
                elif pin_id == "P2":
                    set_servo(pin2, angle)
                    uart.write("OK: Set P2 to " + str(angle) + "\n")
                else:
                    uart.write("ERROR: Unknown pin " + pin_id + "\n")
            else:
                uart.write("ERROR: Invalid command format. Use '<PIN> <ANGLE>'\n")
        except Exception as e:
            uart.write("ERROR: " + str(e) + "\n")

