from flask import Blueprint, current_app
from flask_socketio import join_room
from flask.templating import render_template
from confluent_kafka import Consumer
from app import socket
from os import environ
from app.assets import lamp, air_cond, humidifier

import json

ip = environ.get("LOCAL_IP")
port = environ.get("KAFKA_PORT")
KAFKA_HOST = f'{ip}:{port}'
TYPES = ["luminosity", "presence", "temperature"]

main = Blueprint('main', __name__)

@main.route('/')
def index():
  return render_template("index.html", types = TYPES)

@main.route('/environment/<type>', methods=['GET'])
def page(type):
  configuration = []
  if (type == "luminosity"):
    configuration = ["luminosidade", "lampada"]
  elif (type == "presence"):
    configuration = ["presença", "umidificador"]
  elif (type == "temperature"):
    configuration = ["termometro", "ar condicionado"]
  else:
    pass # TODO return error msg

  return render_template(
    "space_attribute.html",
    sensor = configuration[0],
    actuator = configuration[1],
    type = type
  )

@socket.on("subscribe")
def subscribe(space_attribute):
  join_room(space_attribute)

  
@socket.on("change_status")
def change_status(config):
  if (config["name"] == "temperature"):
    change_air_cond_status(config)
  elif (config["name"] == "presence"):
    change_presence_status(config)
  else:
    change_luminosity_status(config)

def change_air_cond_status(config):
  client = air_cond.AirCond("50052")
  status = parse_status(config["status"])

  temperature = int(config["temperature"])
  client.change_status(status, temperature)


def change_presence_status(config):
  client = humidifier.Humidifier("50054")
  status = parse_status(config["status"])

  client.change_status(status)

def change_luminosity_status(config):
  client = lamp.Lamp("50053")
  status = parse_status(config["status"])

  client.change_status(status)

def parse_status(status):
  status_bool = False
  if (status == "1"):
    status_bool = True

  return status_bool

def handle_environment(type, context):
  with context:
    conf = {
      "bootstrap.servers": KAFKA_HOST,
      "client.id": type,
      "group.id": type
    }
    
    consumer = Consumer(conf)
    consumer.subscribe([type])
    
    try:
      while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            print( msg.error )
        else:
          actuator = get_actuator_info(type)
          handle_data(type, msg = msg, actuator = actuator)
          
    except KeyboardInterrupt:
      print("deu ruim")
    
    consumer.close()

def get_actuator_info(type):
  response = {}
  if (type == "temperature"):
    client = air_cond.AirCond("50052")
    response = client.request_info()
  elif (type == "luminosity"):
    client = lamp.Lamp("50053")
    response = client.request_info()
  else:
    client = humidifier.Humidifier("50054")
    response = client.request_info()
  
  return response

def handle_data(type, msg = {}, actuator = {}):
  payload = msg.value().decode("utf-8")
  payload = json.loads(payload)
  # if (type == "luminosity"):
  #   import pdb
  #   pdb.set_trace()
  new_payload = {
    "sensor":{
      "name": payload.get("sensor", {}).get("name", ""),
      "value": payload.get("sensor", {}).get("value", "")
    },
    "actuator":{
      "name": actuator.get('name', ""),
      "value": actuator.get('value', ""),
      "temperature": actuator.get('temperature', ""),
    }
  }

  socket.emit("data", new_payload, to=type)
