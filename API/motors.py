from API import herkulex
from API.herkulex import servo

herkulex.connect("/dev/tty.usbserial-FTHBYM92", 115200)
motors = []
torques = []
for mCnt in range(1, 19):
    motors.append(servo(mCnt))



