# from managers.ControlPadManager import ControlPadManager
from commanders.KeyboardCommander import KeyboardCommander
from servers import CommandServer
from sensors.ImageCapturer import ImageCapturer


# control_pad_manager = ControlPadManager()
# control_pad_manager.start_control()

# Red:    (183,   0,  6)
# Yellow: (218, 103,  9)
# Green:  ( 15,  37, 26)
# Blue:   ( 11,  27, 50)


if __name__ == '__main__':

    print("######## Start capturing video")
    # ImageCapturer.get_instance().start_infinite_loop_capture()

    print("######## Start CommandServer")
    CommandServer.run_server()

    print("######## Start KeyboardCommander")
    keyboard_commander = KeyboardCommander()
    keyboard_commander.start()


# FIXME test combinations pick-drop
# FIXME test ControlPadManager


# FIXME recognize color of cube in the center

