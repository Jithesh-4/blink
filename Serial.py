# Raspberry Pi Code for Slave

import serial

# Automatically detect the Arduino port
def detect_arduino_port():
    ports = [f'/dev/ttyUSB{i}' for i in range(10)]  # Assuming the Arduino is connected to one of these ports

    for port in ports:
        try:
            ser = serial.Serial(port, 9600, timeout=1)
            ser.close()
            return port
        except serial.SerialException:
            pass

    raise Exception("Arduino port not found")

arduino_port = detect_arduino_port()
ser = serial.Serial(arduino_port, 9600, timeout=1)

while True:
    if ser.in_waiting > 0:
        message = ser.readline().decode('utf-8').rstrip()
        print(f'Message from Arduino: {message}')
