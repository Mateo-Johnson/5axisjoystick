import serial
from vpython import box, vector, rate

ser = serial.Serial('COM3', 9600)
cube = box(pos=vector(0, 0, 0), size=vector(1, 1, 1))

while True:
    rate(30)
    data = ser.readline().decode().strip()
    xVal, yVal = map(int, data.split(','))
    xMove = (xVal - 512) / 512
    yMove = (yVal - 512) / 512
    cube.pos.x += xMove * 0.1
    cube.pos.y += yMove * 0.1
