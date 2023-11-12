import lamp_pb2, lamp_pb2_grpc
from concurrent import futures
import grpc
import time


class LampServer(lamp_pb2_grpc.LampServicer):
  def __init__(self):
    self.status = True
    super().__init__()
  
  def turnOff(self, request, context):
    self.status = False
    response = lamp_pb2.LampStatus()
    response.status = self.status
    return response
  
  def turnOn(self, request, context):
    self.status = True
    response = lamp_pb2.LampStatus()
    response.status = self.status
    return response
  
  def requestInfo(self, request, context):
    response = lamp_pb2.LampStatus()
    response.status = self.status

    return response
  
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
lamp_pb2_grpc.add_LampServicer_to_server(LampServer(), server)

# listen on port 50053
print('Starting server. Listening on port 50053.')
server.add_insecure_port('[::]:50053')
server.start()

try:
  while True:
    time.sleep(86400)
except KeyboardInterrupt:
  server.stop(0)