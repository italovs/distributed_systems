from flask import Flask
from flask_socketio import SocketIO

socket = SocketIO()

def create_app():
  app = Flask(__name__)

  from app.home_assistant import main
  app.register_blueprint(main)
  
  socket.init_app(app)
  
  return app
