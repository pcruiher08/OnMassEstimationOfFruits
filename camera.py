
import logging
import locale
import os
import subprocess
import sys
import serial

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


print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
target = os.path.join('/tmp', file_path.name)
print('Copying image to', target)
camera_file = camera.file_get(
    file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
camera_file.save(target)
subprocess.call(['xdg-open', target])
camera.exit()