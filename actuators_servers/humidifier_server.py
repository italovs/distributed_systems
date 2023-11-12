import humidifier_pb2, humidifier_pb2_grpc
from concurrent import futures
import grpc
import time


class HumidifierServer(humidifier_pb2_grpc.HumidifierServicer):
  def __init__(self):
    self.status = True
    super().__init__()
  
  def turnOff(self, request, context):
    self.status = False
    response = humidifier_pb2.HumidifierStatus()
    response.status = self.status
    return response
  
  def turnOn(self, request, context):
    self.status = True
    response = humidifier_pb2.HumidifierStatus()
    response.status = self.status
    return response
  
  def requestInfo(self, request, context):
    response = humidifier_pb2.HumidifierStatus()
    response.status = self.status

    return response
  
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
humidifier_pb2_grpc.add_HumidifierServicer_to_server(HumidifierServer(), server)

# listen on port 50054
print('Starting server. Listening on port 50054.')
server.add_insecure_port('[::]:50054')
server.start()

try:
  while True:
    time.sleep(86400)
except KeyboardInterrupt:
  server.stop(0)