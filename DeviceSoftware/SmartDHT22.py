import Adafruit_DHT


class SmartDHT22():

   
    def __init__(self, pin_num):
        self.sensor = Adafruit_DHT.DHT22
        self.pin = pin_num

    def get_temp_celsius(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return temperature

    def get_temp_fahrenheit(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return temperature*1.8+32

    def get_humidity(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return humidity

    
