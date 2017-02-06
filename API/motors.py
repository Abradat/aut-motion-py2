from API import herkulex
from API.herkulex import servo

herkulex.connect("/dev/tty.usbserial-FTHBYM92", 115200)
motors = []
torques = []
check = 0 #means torques off
for mCnt in range(1, 19):
    motors.append(servo(mCnt))
    torques.append(0) # 0 Means torque off



