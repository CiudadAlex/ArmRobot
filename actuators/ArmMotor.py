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

        self.position_servos()

    def position_servos(self):

        self.Arm.Arm_serial_servo_write6(
            self.map_index_angle[1],
            self.map_index_angle[2],
            self.map_index_angle[3],
            self.map_index_angle[4],
            self.map_index_angle[5],
            self.map_index_angle[6],
            1000)

        self.print_positions()
        time.sleep(1)

    def storage_position(self):

        self.map_index_angle = {
            1: 90,
            2: 180,
            3: 0,
            4: 0,
            5: 90,
            6: 180,
        }

        self.position_servos()

    def move_all_to_position(self, angle1, angle2, angle3, angle4, angle5, angle6):

        self.map_index_angle = {
            1: angle1,
            2: angle2,
            3: angle3,
            4: angle4,
            5: angle5,
            6: angle6,
        }

        self.position_servos()

