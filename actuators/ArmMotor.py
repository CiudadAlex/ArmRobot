from Arm_Lib import Arm_Device
import time


class ArmMotor:

    MAX_ANGLE = 180
    MIN_ANGLE = 0
    HOME_ANGLE = 90

    instance = None

    @staticmethod
    def get_instance():
        if ArmMotor.instance is None:
            ArmMotor.instance = ArmMotor()
        return ArmMotor.instance

    def __init__(self, s_step=1):

        self.Arm = Arm_Device()

        self.s_time = 500
        self.s_step = s_step

        self.map_index_angle = {
            1: ArmMotor.HOME_ANGLE,
            2: ArmMotor.HOME_ANGLE,
            3: ArmMotor.HOME_ANGLE,
            4: ArmMotor.HOME_ANGLE,
            5: ArmMotor.HOME_ANGLE,
            6: ArmMotor.HOME_ANGLE,
        }

    def print_positions(self):
        print("#############################")
        for key in range(1, 7):
            print(f"{key}: {self.map_index_angle[key]}")
        print("#############################")

    def move(self, index, more_or_less):

        if more_or_less:
            self.map_index_angle[index] += self.s_step
        else:
            self.map_index_angle[index] -= self.s_step

        self.position_servo(index)

    def move_to_position(self, index, angle):

        self.map_index_angle[index] = angle

        self.position_servo(index)

    def position_servo(self, index):

        if self.map_index_angle[index] > ArmMotor.MAX_ANGLE:
            self.map_index_angle[index] = ArmMotor.MAX_ANGLE
        elif self.map_index_angle[index] < ArmMotor.MIN_ANGLE:
            self.map_index_angle[index] = ArmMotor.MIN_ANGLE

        self.Arm.Arm_serial_servo_write(index, self.map_index_angle[index], self.s_time)
        self.print_positions()
        time.sleep(0.01)

    def home(self):

        self.map_index_angle = {
            1: ArmMotor.HOME_ANGLE,
            2: ArmMotor.HOME_ANGLE,
            3: ArmMotor.HOME_ANGLE,
            4: ArmMotor.HOME_ANGLE,
            5: ArmMotor.HOME_ANGLE,
            6: ArmMotor.HOME_ANGLE,
        }

        self.Arm.Arm_serial_servo_write6(ArmMotor.HOME_ANGLE, ArmMotor.HOME_ANGLE, ArmMotor.HOME_ANGLE, ArmMotor.HOME_ANGLE, ArmMotor.HOME_ANGLE, ArmMotor.HOME_ANGLE, 1000)
        self.print_positions()
        time.sleep(1)


