from managers.KnownPositionsManager import KnownPositionsManager
from utils.ColorAverager import ColorAverager
import time


class ColorPositionerTaskPerformer:

    instance = None

    @staticmethod
    def get_instance():
        if ColorPositionerTaskPerformer.instance is None:
            ColorPositionerTaskPerformer.instance = ColorPositionerTaskPerformer()
        return ColorPositionerTaskPerformer.instance

    def __init__(self):
        self.known_positions_manager = KnownPositionsManager.get_instance()

    def check_and_act(self):

        self.known_positions_manager.look()
        time.sleep(5)

        avg_color = ColorAverager.get_average_central_color("./capture.jpg", proportion=0.05)
        color_name = self.get_color_name(avg_color)

        if color_name is None:
            print("No Color detected")
        else:
            self.known_positions_manager.seq_pick_color1_color2(KnownPositionsManager.CENTER, color_name)

    # Red:    (183,   0,  6)
    # Yellow: (218, 103,  9)
    # Green:  ( 15,  37, 26)
    # Blue:   ( 11,  27, 50)

    def get_color_name(self, avg_color):

        r = avg_color[0]
        g = avg_color[1]
        b = avg_color[2]
        return None


