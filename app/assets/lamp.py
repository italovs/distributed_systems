import app.assets.base_actuator
import app.assets.lamp_pb2 as lamp_pb
import app.assets.lamp_pb2_grpc as lamp_pb_grpc

class Lamp(app.assets.base_actuator.BaseActuator):
  def __init__(self, port):
    super().__init__(port)
    self.stub = lamp_pb_grpc.LampStub(self.channel)

  def change_status(self, status):
    self.status = lamp_pb.LampStatus(status = status)
    if (status):
      self.stub.turnOn(self.status)
    else:
      self.stub.turnOff(self.status)
    
  def request_info(self):
    request = lamp_pb.LampInfoParams()
    response = self.stub.requestInfo(request)
    
    return self.build_json(response)
  
  def build_json(self, response_status):
    payload = {
      "name": "lampada",
      "value": response_status.status,
    }
    
    return payload
  