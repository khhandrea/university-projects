python ../program/RegisterCarProgram.py &

# 상허문 : port 60606

python ../program/ParkingManagerProgram.py --position=상허문 &
python ../program/CarRecogProgram.py --position=상허문_입차방향 &
python ../program/CarRecogProgram.py --position=상허문_출차방향 &
python ../program/CrossingGateProgram.py --position=상허문_입차방향 &
python ../program/CrossingGateProgram.py --position=상허문_출차방향 &
python ../program/LoopCoilSensorServer.py --position=상허문_입차방향 &
python ../program/LoopCoilSensorServer.py --position=상허문_출차방향 &
python ../program/DisplayProgram.py --position=상허문_입차방향 &
python ../program/DisplayProgram.py --position=상허문_출차방향 &


# 일감문 : port 60706

python ../program/ParkingManagerProgram.py --position=일감문 &
python ../program/CarRecogProgram.py --position=일감문_입차방향 &
python ../program/CarRecogProgram.py --position=일감문_출차방향 &
python ../program/CrossingGateProgram.py --position=일감문_입차방향 &
python ../program/CrossingGateProgram.py --position=일감문_출차방향 &
python ../program/LoopCoilSensorServer.py --position=일감문_입차방향 &
python ../program/LoopCoilSensorServer.py --position=일감문_출차방향 &
python ../program/DisplayProgram.py --position=일감문_입차방향 &
python ../program/DisplayProgram.py --position=일감문_출차방향 &
python ../program/PayProgram.py --position=일감문 &

# 건국문 : port 60806

python ../program/ParkingManagerProgram.py --position=건국문 &
python ../program/CarRecogProgram.py --position=건국문_입차방향 &
python ../program/CarRecogProgram.py --position=건국문_출차방향 &
python ../program/CrossingGateProgram.py --position=건국문_입차방향 &
python ../program/CrossingGateProgram.py --position=건국문_출차방향 &
python ../program/LoopCoilSensorServer.py --position=건국문_입차방향 &
python ../program/LoopCoilSensorServer.py --position=건국문_출차방향 &
python ../program/DisplayProgram.py --position=건국문_입차방향 &
python ../program/DisplayProgram.py --position=건국문_출차방향 &
python ../program/PayProgram.py --position=건국문 &


# DB용 MQTT : port 60906

python ../program/SchoolDBHandler.py &
python ../program/ParkingDBHandler.py &
python ../program/LogDBHandler.py &

python ../demo/DemoCameraProgram.py &
python ../demo/DemoCrossingGateProgram.py &
python ../demo/DemoDisplayProgram.py &
python ../demo/DemoLoopCoilSensorProgram.py &
python ../demo/DemoPayModuleProgram.py &