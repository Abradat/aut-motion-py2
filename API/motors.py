from API import herkulex
from API.herkulex import servo

herkulex.connect("/dev/tty.usbserial-FTHBYM92", 115200)
motors = []
for mCnt in range(1, 19):
    motors.append(servo(mCnt))

#print(motors[4].get_servo_angle())
#print(type(motors[1].get_servo_position()))
#motors[4].set_led(0x02)
#print(motors[4].get_servo_angle())
#a = servo(5)
#a.set_led(0x02)


