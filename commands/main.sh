RegisterCarProgram.py &

# 상허문 : port 60606

Manager_ParkingManagerProgram.py --position=”상허문” &
CarRecogProgram.py --position=”상허문_입차방향” &
CarRecogProgram.py --position=”상허문_출차방향” &
CrossingGateProgram.py --position=”상허문_입차방향” &
CrossingGateProgram.py --position=”상허문_출차방향” &
LoopCoilSensorServer.py --position=”상허문_입차방향” &
LoopCoilSensorServer.py --position=”상허문_출차방향” &
DisplayProgram.py --position=”상허문_입차방향” &
DisplayProgram.py --position=”상허문_출차방향” &


# 일감문 : port 60706

Manager_ParkingManagerProgram.py --position=”일감문” &
CarRecogProgram.py --position=”일감문_입차방향” &
CarRecogProgram.py --position=”일감문_출차방향” &
CrossingGateProgram.py --position=”일감문_입차방향” &
CrossingGateProgram.py --position=”일감문_출차방향” &
LoopCoilSensorServer.py --position=”일감문_입차방향” &
LoopCoilSensorServer.py --position=”일감문_출차방향” &
DisplayProgram.py --position=”일감문_입차방향” &
DisplayProgram.py --position=”일감문_출차방향” &
PayProgram.py --position=”일감문” &

# 건국문 : port 60806

Manager_ParkingManagerProgram.py --position=”건국문” &
CarRecogProgram.py --position=”건국문_입차방향” &
CarRecogProgram.py --position=”건국문_출차방향” &
CrossingGateProgram.py --position=”건국문_입차방향” &
CrossingGateProgram.py --position=”건국문_출차방향” &
LoopCoilSensorServer.py --position=”건국문_입차방향” &
LoopCoilSensorServer.py --position=”건국문_출차방향” &
DisplayProgram.py --position=”건국문_입차방향” &
DisplayProgram.py --position=”건국문_출차방향” &
PayProgram.py --position=”건국문” &


# DB용 MQTT : port 60906

SchoolDBHandler.py &
ParkingDBHandler.py &
LogDBHandler.py