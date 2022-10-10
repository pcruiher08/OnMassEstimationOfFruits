import time
import serial

ser = serial.Serial(
    port='ttyUSB0',
    baudrate=9600,
ser = serial.Serial('/dev/ttyUSB0', 9600)

while True:
    data = ser.readline()
    if data:
        print(data)
    timeout=1,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)
ser.isOpen()

while 1 :
        bytesToRead = ser.inWaiting()
        data = ser.read(bytesToRead)
        time.sleep(1)
        print(data)