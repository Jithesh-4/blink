# Raspberry Pi Code for Slave

import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)  # Replace '/dev/ttyUSB0' with the actual port

while True:
    if ser.in_waiting > 0:
        message = ser.readline().decode('utf-8').rstrip()
        print(f'Message from Arduino: {message}')
