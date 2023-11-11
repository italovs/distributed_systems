from flask import Blueprint, current_app
from flask_socketio import join_room
from flask.templating import render_template
from confluent_kafka import Consumer
from app import socket
from os import environ
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
  print(space_attribute)
  socket.emit("teste", "teste", to=space_attribute)
  
@socket.on("change_status")
def change_status(actuator, value):
  # TODO - call grpc
  pass

@socket.on("change_temperature")
def change_temperature(value):
  # TODO - call grpc
  pass

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
          handle_data(msg, type)
          
    except KeyboardInterrupt:
      print("deu ruim")
    
    consumer.close()
  
def handle_data(msg, type):
  payload = msg.value().decode("utf-8")
  payload = json.loads(payload)
  
  new_payload = {
    "sensor":{
      "name": payload["sensor"]["name"],
      "value": payload["sensor"]["value"]
    },
    "actuator":{
      "name": "",
      "value": "",
      "temperature": "",
    }
  }
  socket.emit("data", new_payload, to=type)
