
import serial
import time

# Create a serial object (change '/dev/ttyUSB0' to your Arduino's serial port)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

while True:
    # Read data from Arduino
    data = ser.readline().decode().strip()  # Decode bytes to string and strip newline characters
    
    if data:
        print("Data received from Arduino:", data)
        
        # Send acknowledgment or response back to Arduino
        ser.write("Received: ".encode() + data.encode())
        
    time.sleep(0.5)  # Adjust delay as needed


Arduino code for Master (communicating with the Raspberry Pi as slave):

arduino
void setup() {
  Serial.begin(9600);  // Initialize serial communication
}

void loop() {
  // Send data to Raspberry Pi
  Serial.println("Hello Raspberry Pi!");
  delay(1000); // Adjust delay as needed
}


