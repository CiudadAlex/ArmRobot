from actuators.ArmMotor import ArmMotor
import time


class KnownPositionsManager:

    OPEN_CLAW = 90
    CLOSE_CLAW = 135

    POSITION_2_AVOID_TOUCH = 50

    HOME = [90, 90, 90, 90, 90, 90]
    STORAGE = [90, 180, 0, 0, 90, 180]

    CENTER = "center"
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"
    BLUE = "blue"

    MAP_COLOR_POSITIONS_1_5 = {
        CENTER:  [90, 26, 86,  0, 90],
        RED:    [115, 20, 76, 40, 90],
        YELLOW:  [65, 20, 76, 40, 90],
        GREEN:  [145, 20, 76, 40, 90],
        BLUE:    [35, 20, 76, 40, 90],
    }

    MIDDLE_CLOSE_CLAW = [90, 75, 76, 0, 90, CLOSE_CLAW]

    @staticmethod
    def get_positions(color, open_claw):

        if open_claw:
            list_to_add = [KnownPositionsManager.OPEN_CLAW]
        else:
            list_to_add = [KnownPositionsManager.CLOSE_CLAW]

        return KnownPositionsManager.MAP_COLOR_POSITIONS_1_5[color] + list_to_add

    def get_sequence(self, color, pick_or_drop):

        wait_secs = 1.5
        first_open = pick_or_drop

        pick_up_color_move_1 = self.get_positions(color, open_claw=first_open)
        pick_up_color_move_2 = self.get_positions(color, open_claw=not first_open)

        pick_up_color_move_0 = pick_up_color_move_1.copy()
        pick_up_color_move_0[1] = KnownPositionsManager.POSITION_2_AVOID_TOUCH

        pick_up_color_move_3 = pick_up_color_move_2.copy()
        pick_up_color_move_3[1] = KnownPositionsManager.POSITION_2_AVOID_TOUCH

        return [pick_up_color_move_0, wait_secs,
                pick_up_color_move_1, wait_secs,
                pick_up_color_move_2, wait_secs,
                pick_up_color_move_3, wait_secs,
                KnownPositionsManager.MIDDLE_CLOSE_CLAW, wait_secs]

    PICK_UP_CENTER_OPEN_CLAW = get_positions(CENTER, True)

    SEQ_PICK_CENTER = get_sequence(CENTER, pick_or_drop=True)
    SEQ_DROP_CENTER = get_sequence(CENTER, pick_or_drop=False)

    SEQ_PICK_RED = get_sequence(RED, pick_or_drop=True)
    SEQ_DROP_RED = get_sequence(RED, pick_or_drop=False)

    SEQ_PICK_YELLOW = get_sequence(YELLOW, pick_or_drop=True)
    SEQ_DROP_YELLOW = get_sequence(YELLOW, pick_or_drop=False)

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

