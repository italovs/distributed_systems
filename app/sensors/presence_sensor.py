from base_sensor import BaseSensor
import random

class PresenceSensor(BaseSensor):
  def __init__(self, name):
    super().__init__("presence", name)
  
  def generate_value(self):
    self.value = bool(random.getrandbits(1))

sensor = PresenceSensor("Presença")
sensor.run()