from managers.KnownPositionsManager import KnownPositionsManager
from utils.ImagePositionDiscoverer import ImagePositionDiscoverer
from utils.ColorDeterminer import ColorDeterminer
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

        average_position = ImagePositionDiscoverer.get_central_position_of_filtered_pixels("./capture.jpg", filter_of_pixels=ColorDeterminer.is_red)




