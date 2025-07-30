from actuators.ArmMotor import ArmMotor
import time


class KnownPositionsManager:

    OPEN_CLAW = 90
    CLOSE_CLAW = 135

    HOME = [90, 90, 90, 90, 90, 90]
    STORAGE = [90, 180, 0, 0, 90, 180]

    PICK_UP_CENTER_OPEN_CLAW = [90, 26, 86, 0, 90, OPEN_CLAW]
    PICK_UP_CENTER_CLOSE_CLAW = [90, 26, 86, 0, 90, CLOSE_CLAW]

    PICK_UP_RED_OPEN_CLAW = [115, 20, 76, 40, 90, OPEN_CLAW]
    PICK_UP_RED_CLOSE_CLAW = [115, 20, 76, 40, 90, CLOSE_CLAW]

    PICK_UP_YELLOW_OPEN_CLAW = [65, 20, 76, 40, 90, OPEN_CLAW]
    PICK_UP_YELLOW_CLOSE_CLAW = [65, 20, 76, 40, 90, CLOSE_CLAW]

    MIDDLE_CLOSE_CLAW = [90, 75, 76, 0, 90, CLOSE_CLAW]

    SEQ_PICK_CENTER = [PICK_UP_CENTER_OPEN_CLAW, 2,
                       PICK_UP_CENTER_CLOSE_CLAW, 2,
                       MIDDLE_CLOSE_CLAW, 2]

    SEQ_DROP_CENTER = [PICK_UP_CENTER_CLOSE_CLAW, 2,
                       PICK_UP_CENTER_OPEN_CLAW, 2,
                       MIDDLE_CLOSE_CLAW, 2]

    SEQ_PICK_RED = [PICK_UP_RED_OPEN_CLAW, 2,
                       PICK_UP_RED_CLOSE_CLAW, 2,
                       MIDDLE_CLOSE_CLAW, 2]

    SEQ_DROP_RED = [PICK_UP_RED_CLOSE_CLAW, 2,
                       PICK_UP_RED_OPEN_CLAW, 2,
                       MIDDLE_CLOSE_CLAW, 2]

    SEQ_PICK_YELLOW = [PICK_UP_YELLOW_OPEN_CLAW, 2,
                       PICK_UP_YELLOW_CLOSE_CLAW, 2,
                       MIDDLE_CLOSE_CLAW, 2]

    SEQ_DROP_YELLOW = [PICK_UP_YELLOW_CLOSE_CLAW, 2,
                       PICK_UP_YELLOW_OPEN_CLAW, 2,
                       MIDDLE_CLOSE_CLAW, 2]

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

        for list_angles_or_secs in sequence:

            if isinstance(list_angles_or_secs, (int, float)):
                secs_wait = list_angles_or_secs
                time.sleep(secs_wait)
            else:
                list_angles = list_angles_or_secs
                self.move(list_angles)

    ##########################################

    def home(self):
        self.move(KnownPositionsManager.HOME)

    def storage(self):
        self.move(KnownPositionsManager.STORAGE)

    def pick_center(self):
        self.move(KnownPositionsManager.PICK_UP_CENTER_OPEN_CLAW)

    def seq_pick_center(self):
        self.move_sequence(KnownPositionsManager.SEQ_PICK_CENTER)

    def seq_pick_center_red(self):
        self.move_sequence(KnownPositionsManager.SEQ_PICK_CENTER + KnownPositionsManager.SEQ_DROP_RED)

    def seq_pick_center_yellow(self):
        self.move_sequence(KnownPositionsManager.SEQ_PICK_CENTER + KnownPositionsManager.SEQ_DROP_YELLOW)

    def seq_pick_red_center(self):
        self.move_sequence(KnownPositionsManager.SEQ_PICK_RED + KnownPositionsManager.SEQ_DROP_CENTER)

    def seq_pick_red_yellow(self):
        self.move_sequence(KnownPositionsManager.SEQ_PICK_RED + KnownPositionsManager.SEQ_DROP_YELLOW)

    def seq_pick_yellow_center(self):
        self.move_sequence(KnownPositionsManager.SEQ_PICK_YELLOW + KnownPositionsManager.SEQ_DROP_CENTER)

    def seq_pick_yellow_red(self):
        self.move_sequence(KnownPositionsManager.SEQ_PICK_YELLOW + KnownPositionsManager.SEQ_DROP_RED)

