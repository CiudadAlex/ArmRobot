import os
from actuators.ArmMotor import ArmMotor
from managers.KnownPositionsManager import KnownPositionsManager


class Commander:

    COMMAND_MOVE = "move"
    COMMAND_KNOWN = "known"
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
            Commander.COMMAND_KNOWN: self.known,
            Commander.COMMAND_EXIT: self.exit,
        }

        self.help_map = {
            Commander.COMMAND_MOVE: "($index) ($angle, +, -)",
            Commander.COMMAND_KNOWN: "(home, storage, pick_center, seq_pick_center)",
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
        elif subcommand == "pick_center":
            self.known_positions_manager.pick_center()
        elif subcommand == "seq_pick_center":
            self.known_positions_manager.seq_pick_center()
        else:
            print(f"Unknown subcommand: {subcommand}")

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
            func(args)

            if debug:
                print("Executed")
            return True

    @staticmethod
    def help_commands():
        print("Command list:")

        help_map = Commander.get_instance().help_map
        for command in help_map.keys():
            print(f"{command} {help_map[command]}")

