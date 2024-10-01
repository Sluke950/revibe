import obd  # Import the OBD library
import bluetooth  # Import the Bluetooth library

# Define the Bluetooth address of your OBD-II reader
OBD2_BLUETOOTH_ADDRESS = "XX:XX:XX:XX:XX:XX"  # Replace with your OBD-II reader's address

def main():
    # Attempt to connect to the OBD-II device via Bluetooth
    try:
        # Create an OBD connection using Bluetooth
        connection = obd.OBD(portstr=OBD2_BLUETOOTH_ADDRESS)  # Assuming using Bluetooth
        print("Connected to OBD-II device.")
    except Exception as e:
        print(f"Failed to connect to OBD-II device: {e}")
        return

    # Create a command to get RPM
    rpm_command = obd.commands.RPM

    while True:
        # Send the RPM command and get the response
        response = connection.query(rpm_command)

        # Check if the response is valid
        if response.is_null():
            print("No RPM data received.")
        else:
            # Print the RPM value
            print(f"Current RPM: {response.value} RPM")

        # Wait a bit before the next query
        time.sleep(1)  # Adjust the sleep time as needed

if __name__ == "__main__":
    main()
