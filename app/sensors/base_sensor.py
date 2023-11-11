from confluent_kafka import Producer
from os import environ
import time

ip = environ.get("LOCAL_IP")
port = environ.get("KAFKA_PORT")

class BaseSensor:
  def __init__(self, topic, name):
    conf = {
      "bootstrap.servers": f'{ip}:{port}',
      "client.id": "sensor"
    }

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
    pass