from flask import Flask
from flask_socketio import SocketIO

import threading

socket = SocketIO()

def create_app():
  app = Flask(__name__)

  from app.home_assistant import main
  app.register_blueprint(main)
  
  socket.init_app(app)

  from app.home_assistant import TYPES, handle_environment
  print("Starting consumers")
  for type in TYPES:
    thread = threading.Thread(target=handle_environment, args=(type, app.app_context()))
    thread.start()

  return app
