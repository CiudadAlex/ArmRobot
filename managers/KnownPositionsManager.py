from actuators.ArmMotor import ArmMotor
import time


class KnownPositionsManager:

    OPEN_CLAW = 90
    CLOSE_CLAW = 135

    HOME = [90, 90, 90, 90, 90, 90]
    STORAGE = [90, 180, 0, 0, 90, 180]

    PICK_UP_CENTER_OPEN_CLAW = [90, 26, 86, 0, 90, OPEN_CLAW]
    PICK_UP_CENTER_CLOSE_CLAW = [90, 26, 86, 0, 90, CLOSE_CLAW]

    MIDDLE_CLOSE_CLAW = [90, 75, 76, 0, 90, CLOSE_CLAW]

    instance = None

    @staticmethod
    def get_instance():
        if KnownPositionsManager.instance is None:
            KnownPositionsManager.instance = KnownPositionsManager()
        return KnownPositionsManager.instance

    def __init__(self):
        self.arm_motor = ArmMotor.get_instance()

    def move(self, list_angles):
        self.arm_motor.move_all_to_position(*list_angles)

    def move_sequence(self, sequence):

        for list_angles in sequence:
            self.move(list_angles)
            time.sleep(3)

    ##########################################

    def home(self):
        self.move(KnownPositionsManager.HOME)

    def storage(self):
        self.move(KnownPositionsManager.STORAGE)

    def pick_center(self):
        self.move(KnownPositionsManager.PICK_UP_CENTER_OPEN_CLAW)

    def seq_pick_center(self):
        self.move_sequence([
            KnownPositionsManager.PICK_UP_CENTER_OPEN_CLAW,
            KnownPositionsManager.PICK_UP_CENTER_CLOSE_CLAW,
            KnownPositionsManager.MIDDLE_CLOSE_CLAW])


