from managers.KnownPositionsManager import KnownPositionsManager
from utils.ImagePositionDiscoverer import ImagePositionDiscoverer
from utils.ColorDeterminer import ColorDeterminer
from actuators.ArmMotor import ArmMotor
import time
import threading


class RandomPositionColorPositionerTaskPerformer:

    instance = None

    @staticmethod
    def get_instance():
        if RandomPositionColorPositionerTaskPerformer.instance is None:
            RandomPositionColorPositionerTaskPerformer.instance = RandomPositionColorPositionerTaskPerformer()
        return RandomPositionColorPositionerTaskPerformer.instance

    def __init__(self):
        self.known_positions_manager = KnownPositionsManager.get_instance()
        self.running = False
        self.thread = None
        self.arm_motor = ArmMotor.get_instance()
        self.filter_of_pixels = ColorDeterminer.is_red

    def start_infinite_loop_check_and_act(self):
        self.thread = threading.Thread(target=self.infinite_loop_check_and_act)
        self.thread.daemon = True
        self.thread.start()

    def infinite_loop_check_and_act(self):

        self.running = True

        while self.running:
            self.check_and_act()

    def stop(self):
        self.running = False

    def get_color_vectorial_position(self):
        return ImagePositionDiscoverer.get_vectorial_position_of_filtered_pixels("./capture.jpg", filter_of_pixels=self.filter_of_pixels)

    def check_and_act(self):

        vectorial_position = self.search_cube_until_finding()

        if not self.running:
            return

        # Cube found. Get it in the center
        print(f"Cube found. Center in vectorial position: {vectorial_position}")

        moved = self.move_arm_until_enough_centered()

    def move_arm_until_enough_centered(self):

        x, y = self.get_color_vectorial_position()
        moved = False

        # Red to the left. Yellow to the right

        if x > 15:
            self.arm_motor.move(1, more_or_less=False)
            moved = True
        elif x < -15:
            self.arm_motor.move(1, more_or_less=True)
            moved = True

        if y > 15:
            self.arm_motor.move(2, more_or_less=True)
            moved = True
        elif y < -15:
            self.arm_motor.move(2, more_or_less=True)
            moved = True

        return moved


    def search_cube_until_finding(self):

        self.known_positions_manager.look()
        current_angle = KnownPositionsManager.LOOK[0]
        current_dir_asc = True

        time.sleep(3)

        vectorial_position = self.get_color_vectorial_position()

        while self.running and vectorial_position is None:
            current_angle, current_dir_asc = self.search_cube_step(current_angle, current_dir_asc=current_dir_asc)
            time.sleep(2)
            vectorial_position = self.get_color_vectorial_position()

        return vectorial_position

    def search_cube_step(self, current_angle, current_dir_asc):

        if current_angle > 115:
            angle1 = self.arm_motor.move(1, more_or_less=False)
            return angle1, False
        elif current_angle < 65:
            angle1 = self.arm_motor.move(1, more_or_less=True)
            return angle1, True

        angle1 = self.arm_motor.move(1, more_or_less=current_dir_asc)
        return angle1, current_dir_asc


