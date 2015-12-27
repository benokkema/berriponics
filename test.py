import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')
pin10 = board.get_pin('d:10:p')
pin9 = board.get_pin('d:9:p')

def forward():
    pin10.write(1.0)
    pin9.write(0)

def reverse():
    pin9.write(1.0)
    pin10.write(0)

def stop():
    pin9.write(0)
    pin10.write(0)
"""
for i in range(10):
    forward()
    print(i+1)
    time.sleep(1)
    stop()
    time.sleep(2)
"""
forward()
time.sleep(2)
reverse()
time.sleep(2)
stop()

board.exit()

