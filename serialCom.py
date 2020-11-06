import json
import requests
import redis
import websocket
import serial
import time


ws=websocket.WebSocket()
ser = serial.Serial('COM3',9600, timeout=2)
time.sleep(3)

ws.connect('ws://localhost:8000/ws/polData/')

def getValues():
    ser.write(b'y')
    arduinoData = ser.readline().decode().split('\r\n')
    return arduinoData[0]

result =  ws.recv()
while True:
    data1 = getValues()
    data2 = data1
    ws.send(json.dumps({'temp_N':data1,'temp_B':data2}))


        