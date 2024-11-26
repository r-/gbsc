import serial
import time

# Configure the serial connection to the micro:bit
microbit_port = "/dev/ttyACM0"  # Update if needed
baud_rate = 115200

# Function to send a command to the micro:bit
def send_command(ser, command):
    ser.write((command + "\n").encode('utf-8'))  # Send command over UART
    time.sleep(0.1)  # Small delay to allow the micro:bit to respond
    response = ser.readline().decode('utf-8').strip()  # Read the response
    if response:
        print(f"Micro:bit response: {response}")
    else:
        print("No response from micro:bit.")

try:
    # Open the serial connection
    with serial.Serial(microbit_port, baud_rate, timeout=1) as ser:
        print("Connected to micro:bit.")

        # Read the initialization message
        response = ser.readline().decode('utf-8').strip()
        print(f"Micro:bit initialization: {response}")

        # Main loop: Allow user to send commands to control servos
        while True:
            command = input("Enter command (e.g., P0 90, P1 45, P2 180, EXIT): ").strip().upper()
            if command == "EXIT":
                print("Exiting.")
                break
            send_command(ser, command)

except serial.SerialException as e:
    print(f"Error: {e}")
