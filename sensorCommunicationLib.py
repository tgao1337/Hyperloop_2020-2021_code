import time
import board
import busio
import adafruit_tmp006
import RPi.GPIO as GPIO

#Code for sensors communication



#Code for reading from SparkFun IMU Breakout: Sagarika



#Code for Writing to SparkFun IMU Breakout: Sagarika



#Code for Reading from 19MM DIGITAL OUTPUT PRESSURE SENSOR



#Code for Writing to 19MM DIGITAL OUTPUT PRESSURE SENSOR



#Code for Reading from MAX31865: Luiza
import time # Will print the temperature every second.
import board
import busio
import digitalio
import adafruit_max31865
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5) # Chip select of the MAX31865 board.
sensor = adafruit_max31865.MAX31865(spi, cs, wires=3)
sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=100.0, ref_resistor=430.0)

print(‘Resistance: {0:0.3f} Ohms’.format(sensor.resistance))

# Main loop to print the temperature every second.
while True:
  # Read temperature.
  temp = sensor.temperature
  # Print the value.
  print(‘Temperature: {0:0.3f}C’.format(temp))
  # Delay for a second.
  time.sleep(1.0)


#Code for Writing to MAX31865: Luiza
#want to verify that the read is woking prior to writing to the MAX31865


#Code for Reading from TMP006 Contact-less Infrared Thermopile Sensor: Demitri

def get_temp_ncontact():
    # Define a function to convert celsius to fahrenheit.
    def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

    # Create library object using Bus I2C port
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_tmp006.TMP006(i2c)

    # Initialize communication with the sensor, using the defaul16 samples
    # This is the best accuracy but a little slower at reacting to changes.
    # The first sample will be meaningless
    while True:
        obj_temp = sensor.temperature
        print('Object temperature: {0:0.3F}*C / {1:0.3F}*F'.format(obj_temp, c_to_f(obj_temp)))
        time.sleep(5.0)




#Code to REad from ELEGOO HC-SR04: Alex
def get_distance():
  GPIO.setmode(GPIO.BCM)

  TRIG = 23 # output pin
  ECHO = 24 # input pin

  GPIO.setup(TRIG, GPIO.OUT)
  GPIO.setup(ECHO, GPIO.IN)

  GPIO.output(TRIG, False)
  time.sleep(1) # Give sensor a second to settle

  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO) == 0:
    pulse_start = time.time()

  while GPIO.input(ECHO) == 1:
    pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start
  
  # Assume speed of sound to be 343 m/s
  # Distance here is measured in cm
  distance = (pulse_duration * 17150).round(3)
  
  return distance



#Code to Write to ELEGOO HC-SR04: Alex 



#Code for 3202 Mini Spy Camera: Tommy
# move this init to the beginning later on
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, 1)

def take_pic():
    GPIO.output(26, 0)
    time.sleep(0.05)
    GPIO.output(26, 1)
    
def record_vid(time_in_seconds):
    GPIO.output(26, 0)
    time.sleep(.6)
    GPIO.output(26, 1)
    time.sleep(time_in_seconds)  # may not help if using other sensors
    GPIO.output(26, 0)
    time.sleep(.6)
    GPIO.output(26, 1)


#Code to Write to 3202 Mini Spy Camera



#Code to Read from the Pressure Sensor-



#Code to Write to the Pressure Sensor
