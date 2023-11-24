import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Set the GPIO pin to which the LED is connected
led_pin = 11
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        # Turn on the LED
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)  # Sleep for 1 second

        # Turn off the LED
        GPIO.output(led_pin, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)  # Sleep for 1 second

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    # Clean up the GPIO pins
    GPIO.cleanup()
