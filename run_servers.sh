#!/bin/bash

mosquitto -v -p 60106 & # for dummy
mosquitto -v -p 60406 & # 차량 등록 서버
mosquitto -v -p 60506 & # demo cli input
mosquitto -v -p 60507 & # demo cli print
mosquitto -v -p 60606 & # 상허문
mosquitto -v -p 60706 & # 일감문
mosquitto -v -p 60806 & # 건국문
mosquitto -v -p 60906   # DB용