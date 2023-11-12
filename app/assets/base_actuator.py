import grpc

class BaseActuator():
  def __init__(self, port):
    self.channel = grpc.insecure_channel(f'localhost:{port}')
    self.stub = ""
    self.status = ""

  
  def turnOn(self):
    self.stub.turnOn(self.status)

  
  def turnOff(self):
    self.stub.turnOff(self.status)

  def build_json(response_status):
    payload = {
      "name": response_status.name,
      "value": response_status.status
    }
    
    return payload