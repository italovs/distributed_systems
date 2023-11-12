import app.assets.base_actuator
import app.assets.humidifier_pb2 as humidifier_pb
import app.assets.humidifier_pb2_grpc as humidifier_pb_grpc

class Humidifier(app.assets.base_actuator.BaseActuator):
  def __init__(self, port):
    super().__init__(port)
    self.stub = humidifier_pb_grpc.HumidifierStub(self.channel)

  def change_status(self, status):
    self.status = humidifier_pb.HumidifierStatus(status = status)
    if (status):
      self.stub.turnOn(self.status)
    else:
      self.stub.turnOff(self.status)
    
  def request_info(self):
    request = humidifier_pb.HumidifierInfoParams()
    response = self.stub.requestInfo(request)
    
    return self.build_json(response)
  
  def build_json(self, response_status):
    payload = {
      "name": "humidificador",
      "value": response_status.status,
    }
    
    return payload
  