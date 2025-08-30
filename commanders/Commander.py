import os
import traceback
from actuators.ArmMotor import ArmMotor
from managers.KnownPositionsManager import KnownPositionsManager
from sensors.ImageCapturer import ImageCapturer
from datetime import datetime
from utils.ColorAverager import ColorAverager
from taskperformers.ColorPositionerTaskPerformer import ColorPositionerTaskPerformer
from taskperformers.RandomPositionColorPositionerTaskPerformer import RandomPositionColorPositionerTaskPerformer


class Commander:

    COMMAND_MOVE = "move"
    COMMAND_MOVE_6 = "move6"
    COMMAND_KNOWN = "known"
    COMMAND_PHOTO = "photo"
    COMMAND_COLOR = "color"
    COMMAND_POSITION_BY_COLOR = "position_by_color"
    COMMAND_RANDOM_PLACE_POSITION_BY_COLOR = "random_position"
    COMMAND_EXIT = "exit"

    instance = None

    @staticmethod
    def get_instance():
        if Commander.instance is None:
            Commander.instance = Commander()
        return Commander.instance

    def __init__(self):
        self.arm_motor = ArmMotor.get_instance()
        self.known_positions_manager = KnownPositionsManager.get_instance()

        self.command_map = {
            Commander.COMMAND_MOVE: self.move,
            Commander.COMMAND_MOVE_6: self.move_6,
            Commander.COMMAND_KNOWN: self.known,
            Commander.COMMAND_PHOTO: self.photo,
            Commander.COMMAND_COLOR: self.color,
            Commander.COMMAND_POSITION_BY_COLOR: self.position_by_color,
            Commander.COMMAND_RANDOM_PLACE_POSITION_BY_COLOR: self.random_place_position_by_color,
            Commander.COMMAND_EXIT: self.exit,
        }

        self.help_map = {
            Commander.COMMAND_MOVE: "($index) ($angle, +, -)",
            Commander.COMMAND_MOVE_6: "($angle1) ($angle2) ($angle3) ($angle4) ($angle5) ($angle6)",
            Commander.COMMAND_KNOWN: "(home, storage, look, pick_$color, seq_pick_$color, seq_pick_$color1_$color2)",
            Commander.COMMAND_PHOTO: "",
            Commander.COMMAND_COLOR: "",
            Commander.COMMAND_POSITION_BY_COLOR: "(on off)",
            Commander.COMMAND_RANDOM_PLACE_POSITION_BY_COLOR: "(on off)",
            Commander.COMMAND_EXIT: "",
        }

    def move(self, args):

        index = int(args[0])

        if index == 0:
            self.arm_motor.home()
        elif index == 7:
            self.arm_motor.storage_position()
        else:
            str_angle = args[1]
            self.move_real_index(index, str_angle)

    def move_6(self, args):
        self.arm_motor.move_all_to_position(*args)

    def move_real_index(self, index, str_angle):

        if str_angle == "+":
            self.arm_motor.move(index, more_or_less=True)
        elif str_angle == "-":
            self.arm_motor.move(index, more_or_less=False)
        else:
            angle = int(str_angle)
            self.arm_motor.move_to_position(index, angle)

    def known(self, args):

        subcommand = args[0]

        if subcommand == "home":
            self.known_positions_manager.home()

        elif subcommand == "storage":
            self.known_positions_manager.storage()

        elif subcommand == "look":
            self.known_positions_manager.look()

        elif subcommand.startswith("pick_"):

            list_tokens = subcommand.split("_")
            color_pick = list_tokens[1]
            self.known_positions_manager.pick_color(color_pick)

        elif subcommand.startswith("seq_pick_"):

            list_tokens = subcommand.split("_")

            if len(list_tokens) == 3:
                color_pick = list_tokens[2]
                self.known_positions_manager.seq_pick_color(color_pick)
            else:
                color_pick = list_tokens[2]
                color_drop = list_tokens[3]
                self.known_positions_manager.seq_pick_color1_color2(color_pick, color_drop)

    @staticmethod
    def photo(args):
        str_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        ImageCapturer.capture_image(image_name='photo_' + str_now + '.jpg')

    @staticmethod
    def color(args):
        avg_color = ColorAverager.get_average_central_color("./capture.jpg", proportion=0.05)
        str_color = str(avg_color)
        print(f"COLOR: {str_color}")
        return str_color

    @staticmethod
    def position_by_color(args):

        subcommand = args[0]

        if subcommand == "on":
            ColorPositionerTaskPerformer.get_instance().start_infinite_loop_check_and_act()
        else:
            ColorPositionerTaskPerformer.get_instance().stop()

    @staticmethod
    def random_place_position_by_color(args):

        subcommand = args[0]

        if subcommand == "on":
            RandomPositionColorPositionerTaskPerformer.get_instance().start_infinite_loop_check_and_act()
        else:
            RandomPositionColorPositionerTaskPerformer.get_instance().stop()


    @staticmethod
    def exit(args):
        os._exit(0)

    @staticmethod
    def execute(command_with_args, debug=False):

        list_tokens = command_with_args.split()
        command = list_tokens[0]
        args = list_tokens[1:]

        if command not in Commander.get_instance().command_map.keys():
            Commander.help_commands()
            return False
        else:
            func = Commander.get_instance().command_map[command]

            try:
                func(args)

            except Exception as e:
                print(f"Error executing command: {e}")
                traceback.print_exc()
                Commander.help_commands()
                return False

            if debug:
                print("Executed")
            return True

    @staticmethod
    def help_commands():
        print("Command list:")

        help_map = Commander.get_instance().help_map
        for command in help_map.keys():
            print(f"{command} {help_map[command]}")

