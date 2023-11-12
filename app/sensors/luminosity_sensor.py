from base_sensor import BaseSensor
import random

class LuminositySensor(BaseSensor):
  def __init__(self, name):
    super().__init__("luminosity", name)
  
  def generate_value(self):
    self.value = random.randint(0,100)

sensor = LuminositySensor("Luminosidade")
sensor.run()