# from actuators.ArmMotor import ArmMotor
# from managers.ControlPadManager import ControlPadManager
# import time
from commanders.KeyboardCommander import KeyboardCommander


# control_pad_manager = ControlPadManager()
# control_pad_manager.start_control()

# arm_motor = ArmMotor.get_instance()

# for i in range(100):
#     arm_motor.move(2, True)
#     arm_motor.move(6, True)
#     time.sleep(.2)

if __name__ == '__main__':

    print("######## Start KeyboardCommander")
    keyboard_commander = KeyboardCommander()
    keyboard_commander.start()


