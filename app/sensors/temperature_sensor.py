from base_sensor import BaseSensor
import random

class TemperatureSensor(BaseSensor):
  def __init__(self, name):
    super().__init__("temperature", name)
    
  def generate_value(self):
    self.value = random.randrange(22,29)

sensor = TemperatureSensor("Temperatura")
sensor.run()