from actuators.ArmMotor import ArmMotor
# from managers.ControlPadManager import ControlPadManager
import time


# control_pad_manager = ControlPadManager()
# control_pad_manager.start_control()

arm_motor = ArmMotor()

arm_motor.move(2, True)
time.sleep(1)

arm_motor.move(2, True)
time.sleep(1)

arm_motor.move(2, True)
time.sleep(1)

arm_motor.move(2, True)
time.sleep(1)

arm_motor.move(2, True)
time.sleep(1)
