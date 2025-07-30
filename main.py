# from managers.ControlPadManager import ControlPadManager
# from sensors.ImageCapturer import ImageCapturer
from commanders.KeyboardCommander import KeyboardCommander

# control_pad_manager = ControlPadManager()
# control_pad_manager.start_control()

# image_capturer = ImageCapturer()
# image_capturer.capture_image()


if __name__ == '__main__':

    print("######## Start KeyboardCommander")
    keyboard_commander = KeyboardCommander()
    keyboard_commander.start()


