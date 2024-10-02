import PyOBD as obd
import time

# Replace with the actual serial port (e.g., '/dev/rfcomm0' or '/dev/ttyUSB0')
serial_port = '/dev/rfcomm0'

# Create an OBD connection with the serial port
connection = obd.OBD(port=serial_port)  # Automatically connects to the specified OBD-II interface

# Command to get the Engine RPM
rpm_cmd = obd.commands.RPM

# Function to read engine RPM
def read_engine_rpm():
    response = connection.query(rpm_cmd)  # Send the command
    if response.is_null():
        print("No response from the OBD-II interface.")
    else:
        rpm = response.value.magnitude  # Extract the RPM value
        print(f"Engine RPM: {rpm}")

if __name__ == "__main__":
    try:
        while True:
            read_engine_rpm()
            # Wait for a second before the next reading
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        connection.close()  # Close the OBD connection
