from microbit import *

# Initialize UART for serial communication
uart.init(baudrate=115200)

while True:
    if uart.any():
        command = uart.read().decode('utf-8').strip()  # Read command and strip whitespace
        if command == "PING":
            uart.write("PONG\n")  # Respond with "PONG"
        elif command == "ON":
            display.show(Image.HEART)
            uart.write("LED_ON\n")  # Respond with "LED_ON"
        elif command == "OFF":
            display.clear()
            uart.write("LED_OFF\n")  # Respond with "LED_OFF"
        else:
            uart.write("UNKNOWN\n")  # Respond with "UNKNOWN"
