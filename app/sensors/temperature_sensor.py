from app.sensors.base_sensor import BaseSensor
import json
import random

class TemperatureSensor(BaseSensor):
  def __init__(self, name):
    super().__init__("temperature", name)
    
  def change_values(self):
    self.generate_temperature()
    json_message = self.__build_json()
    self.message = json.dumps(json_message)
  
  def generate_temperature(self):
    self.value = random.randrange(22,29)
    pass
    
  def __build_json(self):
    return {
      "sensor":{
        "name": self.name,
        "value": self.value,
      }
    }

sensor = TemperatureSensor("temperatura")
sensor.run()