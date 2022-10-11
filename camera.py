
import logging
import locale
import os
import subprocess
import sys
import serial
import fnmatch
import gphoto2 as gp

weight = 0
#ser = serial.Serial('/dev/ttyUSB0', 9600)

locale.setlocale(locale.LC_ALL, '')
logging.basicConfig(
    format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
callback_obj = gp.check_result(gp.use_python_logging())
camera = gp.Camera()
camera.init()
print('Capturing image')
file_path = camera.capture(gp.GP_CAPTURE_IMAGE)

#data = ser.readline()
data = 0
print('Weight of fruit: {0}'.format(data))

filename = '/media/pcruiher08/phi/dataset/pictures'
photoname = "testname" + str(len(fnmatch.filter(os.listdir(filename), '*.*')) + 1) + ".jpg"
print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
target = os.path.join('/media/pcruiher08/phi/dataset/pictures', photoname)
print('there are {0} files in the folder'.format(len(fnmatch.filter(os.listdir(filename), '*.*'))))
print('Copying image to', target)
camera_file = camera.file_get(
    file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
camera_file.save(target)
subprocess.call(['xdg-open', target])
camera.exit()