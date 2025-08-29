from managers.KnownPositionsManager import KnownPositionsManager
from utils.ColorAverager import ColorAverager
import time
import threading


class ColorPositionerTaskPerformer:

    instance = None

    @staticmethod
    def get_instance():
        if ColorPositionerTaskPerformer.instance is None:
            ColorPositionerTaskPerformer.instance = ColorPositionerTaskPerformer()
        return ColorPositionerTaskPerformer.instance

    def __init__(self):
        self.known_positions_manager = KnownPositionsManager.get_instance()
        self.running = False
        self.thread = None

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

    def check_and_act(self):

        self.known_positions_manager.look()
        time.sleep(5)

        avg_color = ColorAverager.get_average_central_color("./capture.jpg", proportion=0.05)
        color_name = self.get_color_name(avg_color)

        if color_name is None:
            print(f"No Color detected: {avg_color}")
        else:
            print(f"Color {color_name} detected")
            self.known_positions_manager.seq_pick_color1_color2(KnownPositionsManager.CENTER, color_name)

    # Red:    (183,   0,  6)
    # Yellow: (218, 103,  9)
    # Green:  ( 15,  37, 26)
    # Blue:   ( 11,  27, 50)

    @staticmethod
    def get_color_name(avg_color):

        r = avg_color[0]
        g = avg_color[1]
        b = avg_color[2]

        if r > 120 and g < 50 and b < 50:
            return KnownPositionsManager.RED

        elif r > 70 and g > 70 and b < 50:
            return KnownPositionsManager.YELLOW

        elif r < 20 and g > b + 10:
            return KnownPositionsManager.GREEN

        elif r < 20 and b > g + 10:
            return KnownPositionsManager.BLUE

        return None


