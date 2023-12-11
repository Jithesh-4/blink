import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)  # Replace '/dev/ttyUSB0' with the actual port your Arduino is connected to

try:
    while True:
        # Send a request from Raspberry Pi to Arduino
        ser.write(b'R')  # Sending the letter 'R' to request RPM data

        # Wait for the response
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            print(data)
        time.sleep(1)  # Adjust this delay based on your Arduino loop timing
except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")
