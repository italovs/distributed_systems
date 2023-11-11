from flask import Blueprint, current_app
from flask_socketio import join_room
from flask.templating import render_template
from app import socket
import threading

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
    actuator = configuration[1]
  )

@socket.on("subscribe")
def subscribe(space_attribute):
  join_room(space_attribute)
  
@socket.on("change_status")
def change_status(actuator, value):
  # TODO - call grpc
  pass

@socket.on("change_temperature")
def change_temperature(value):
  # TODO - call grpc
  pass

def handle_environment(self, type, app_context):
  app_context.push()
  # TODO - add kafka consumer
  socket.emit("data", "", to=type)


# for type in TYPES:
#   thread = threading.Thread(target=handle_environment, args=(type, current_app.app_context()))
#   thread.start()