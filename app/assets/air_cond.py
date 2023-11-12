import app.assets.base_actuator
import app.assets.air_cond_pb2 as air_cond_pb
import app.assets.air_cond_pb2_grpc as air_cond_pb_grpc

class AirCond(app.assets.base_actuator.BaseActuator):
  def __init__(self, port):
    super().__init__(port)
    self.temperature = ""
    self.stub = air_cond_pb_grpc.AirCondStub(self.channel)
    
  def turnOn(self):
    self.status = air_cond_pb.AirCondStatus(status = True)
    super().turnOn()

  def turnOff(self):
    self.status = air_cond_pb.AirCondStatus(status = False)
    super().turnOff()
    
  def change_status(self, status, temperature):
    self.status = air_cond_pb.AirCondStatus(status = status, temperature = temperature)
    self.stub.changeTemperature(self.status)
  
  
  def change_temperature(self, temperature):
    self.status = air_cond_pb.AirCondStatus(temperature = temperature)
    self.stub.changeTemperature(self.status)
    
  def request_info(self):
    request = air_cond_pb.AirCondInfoParams()
    response = self.stub.requestInfo(request)
    
    return self.build_json(response)
  
  def build_json(self, response_status):
    payload = {
      "name": "ar condicionado",
      "value": response_status.status,
      "temperature": response_status.temperature
    }
    
    return payload
  