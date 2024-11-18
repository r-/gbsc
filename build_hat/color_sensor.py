from buildhat import ColorSensor
import time

# Initialize the color sensor on port C
color_sensor = ColorSensor('C')

print("Color sensor initialized successfully. Detecting colors...")

def identify_color(rgbi):
    """
    Identifies the color based on custom thresholds.
    :param rgbi: List of [R, G, B, I] values
    :return: Detected color as a string
    """
    r, g, b, intensity = rgbi

    # Ensure valid values
    if r <= 10 and g <= 10 and b <= 10:
        return "No color detected or too dark"

    # Custom thresholds for colors
    if r > 50 and g < 50 and b < 40:
        return "Red"
    elif r < 40 and g > 40 and b > 60:
        return "Blue"
    elif r > 180 and g > 120 and b < 150:
        return "Yellow"

    return "Unknown color"

try:
    while True:
        rgbi = color_sensor.get_color_rgbi()

        if rgbi:
            color_name = identify_color(rgbi)
            print(f"Detected color: {color_name} (RGBI: {rgbi})")
        else:
            print("No color detected.")

        time.sleep(0.5)  # Adjust the delay as needed
except KeyboardInterrupt:
    print("\nExiting program...")
