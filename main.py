from commanders.KeyboardCommander import KeyboardCommander
from servers import CommandServer
from sensors.ImageCapturer import ImageCapturer
import sys


MODE_DEFAULT = "default"
MODE_MINIMAL = "minimal"


def get_mode():

    mode = MODE_DEFAULT
    num_command_tokens = len(sys.argv)
    print("Number of command tokens:", num_command_tokens)

    if num_command_tokens == 2:
        mode = sys.argv[1]
        print("Mode:", mode)

    return mode


if __name__ == '__main__':

    selected_mode = get_mode()

    if MODE_DEFAULT == selected_mode:
        print("######## Start capturing video")
        ImageCapturer.get_instance().start_infinite_loop_capture()

        print("######## Start CommandServer")
        CommandServer.run_server()

    print("######## Start KeyboardCommander")
    keyboard_commander = KeyboardCommander()
    keyboard_commander.start()
