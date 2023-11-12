from confluent_kafka import Producer
from os import environ
from dotenv import load_dotenv
import time
import json

load_dotenv()
ip = environ.get("LOCAL_IP")
port = environ.get("KAFKA_PORT")

class BaseSensor:
  def __init__(self, topic, name):
    conf = {
      "bootstrap.servers": f'{ip}:{port}',
      "client.id": "sensor"
    }

    self.value = ""
    self.name = name
    self.topic = topic
    self.producer = Producer(conf)
    
  def run(self):
    while True:
      time.sleep(1)
      self.change_values()
      self.producer.produce(self.topic, value = self.message)
      self.producer.poll()

  def change_values(self):
    self.generate_value()
    json_message = self.__build_json()
    self.message = json.dumps(json_message)
  
  def __build_json(self):
    return {
      "sensor":{
        "name": self.name,
        "value": self.value,
      }
    }
  
  def generate_value(self):
    pass