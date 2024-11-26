import serial
import time

# Configure serial connection
microbit_port = "/dev/ttyACM0"  # Update to match your setup
baud_rate = 115200

try:
    # Establish the serial connection
    with serial.Serial(microbit_port, baud_rate, timeout=1) as ser:
        print("Connected to micro:bit.")

        # Allow time for the micro:bit to reboot
        time.sleep(2)
        
        # Flush the initial output
        ser.reset_input_buffer()

        # Send commands and read responses
        while True:
            command = input("Enter command (PING, ON, OFF, EXIT): ").strip().upper()
            if command == "EXIT":
                print("Exiting.")
                break
            
            try:
                # Send the command to micro:bit
                ser.write((command + "\n").encode('utf-8'))
                
                # Read the response
                response = ser.readline().decode('utf-8').strip()
                if response:
                    print(f"Micro:bit response: {response}")
                else:
                    print("No response from micro:bit.")
            except serial.SerialException as e:
                print(f"Serial communication error: {e}")
                break
except serial.SerialException as e:
    print(f"Error: {e}")
