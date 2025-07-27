from actuators.ArmMotor import ArmMotor
# from managers.ControlPadManager import ControlPadManager
import time


# control_pad_manager = ControlPadManager()
# control_pad_manager.start_control()

arm_motor = ArmMotor()

for i in range(100):
    arm_motor.move(2, True)
    arm_motor.move(6, True)
    time.sleep(.2)

