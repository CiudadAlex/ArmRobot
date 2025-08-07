# from managers.ControlPadManager import ControlPadManager
from commanders.KeyboardCommander import KeyboardCommander
from servers import CommandServer
from sensors.ImageCapturer import ImageCapturer


# control_pad_manager = ControlPadManager()
# control_pad_manager.start_control()

from utils.ColorAverager import ColorAverager
# avg_color = ColorAverager.get_average_central_color("./capture.jpg", proportion=0.05)
# print(f"COLOR: {avg_color}")


if __name__ == '__main__':

    print("######## Start capturing video")
    ImageCapturer.get_instance().start_infinite_loop_capture()

    print("######## Start CommandServer")
    CommandServer.run_server()

    print("######## Start KeyboardCommander")
    keyboard_commander = KeyboardCommander()
    keyboard_commander.start()


# FIXME test combinations pick-drop
# FIXME test ControlPadManager


# FIXME recognize color of cube in the center

