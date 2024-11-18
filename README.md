# G.B.S.C - Great Ball Sorting Contraption

## Overview

The **Great Ball Sorting Contraption (G.B.S.C)** is an innovative project that utilizes **coding**, **sensors**, **motors**, and **servos** to sort and manage balls efficiently. 

The system begins by accepting balls in a storage container, which are then transported to a sorting machine. Using a color sensor, the machine identifies and sorts the balls into different containers based on their colors. Once sorted, the balls are either sent back to the start or forwarded to the next module in the system for further processing.

## Features

- **Automated Sorting**: Uses sensors to identify and sort balls based on color.
- **Efficient Movement**: Powered by motors and servos for precise ball handling.
- **Modular Design**: Allows for integration with additional modules in the system.
- **Scalable**: Designed to accommodate various ball types and system expansions.

## Current Progress

### Hardware:
- **Raspberry Pi**: Acts as the central controller.
- **Explorer HAT**: Connected to various sensors for input/output management.
- **Build HAT**: Manages LEGO-compatible motors and servos.
- **Pneumatic Sensor (Tube Air Pressure Unit)**: Measures pressure for handling components.
- **Lego Color Sensor**: Measures color of the balls.
- **Lego Force Sensor**: Measures force.
- **Lego Distance Sensor**: Measures distance.
- **Lego Engine**: For transportation.
- **SG90 Servos**: For Ball Gates.

### Software:
- Initial code for:
  - **Explorer HAT**: Sensor and motor control.
  - **Build HAT**: LEGO motor and servo handling.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/gbsc.git
   cd gbsc
   ```

2. **Set Up the Environment**:
   - Install necessary dependencies for Raspberry Pi:
     ```bash
     sudo apt-get update
     sudo apt-get install python3-pip
     pip3 install -r requirements.txt
     ```
   - Enable required Raspberry Pi interfaces (I2C, etc.).

3. **Run the Code**:
   - Navigate to the appropriate script and execute:
     ```bash
     python3 main.py
     ```

## Folder Structure

```plaintext
GBSC/
?
??? /explorer_hat/             # Source code for the project
?   ??? pressure_sensor.py     # Code for Explorer HAT
?   ??? utils/                 # Helper functions and utilities
??? /build_hat/                # Source code for the project
?   ??? color_sensor.py        # Code for Explorer HAT
?   ??? force_sensor.py        # Code for Explorer HAT
?   ??? distance_sensor.py        # Code for Explorer HAT
?   ??? utils/                 # Helper functions and utilities
?
??? /docs/                       # Documentation and design files
?
??? /assets/                     # Images, diagrams, or media
?
??? requirements.txt             # Python dependencies
??? README.md                    # Project overview (this file)
??? LICENSE                      # License for the project
```

## Usage

1. Load the balls into the **storage container**.
2. Start the program using:
   ```bash
   python3 main.py
   ```
3. Watch as the balls are automatically sorted into the designated containers!
4. Modify or extend the system with additional modules as needed.

## Future Goals

- Integrate the pneumatic sensor for advanced handling.
- Develop a GUI or web interface for real-time monitoring and control.
- Enhance modularity for seamless integration with other systems.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the [gpl](LICENSE).
