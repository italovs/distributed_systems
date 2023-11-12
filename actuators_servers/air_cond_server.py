import air_cond_pb2, air_cond_pb2_grpc
from concurrent import futures
import grpc
import time


class AirCondServer(air_cond_pb2_grpc.AirCondServicer):
  def __init__(self):
    self.status = True
    self.temperature = 22
    super().__init__()
  
  def changeTemperature(self, request, context):
    self.temperature = request.temperature
    self.status = request.status
    response = air_cond_pb2.AirCondStatus()
    
    response.temperature = self.temperature
    response.status = self.status

    return response
  
  def requestInfo(self, request, context):
    response = air_cond_pb2.AirCondStatus()
    response.status = self.status
    response.temperature = self.temperature

    return response
  
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
air_cond_pb2_grpc.add_AirCondServicer_to_server(AirCondServer(), server)

# listen on port 50052
print('Starting server. Listening on port 50052.')
server.add_insecure_port('[::]:50052')
server.start()

try:
  while True:
    time.sleep(86400)
except KeyboardInterrupt:
  server.stop(0)