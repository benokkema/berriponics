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

forward()

board.exit()

