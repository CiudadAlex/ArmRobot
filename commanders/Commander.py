import os
from actuators.ArmMotor import ArmMotor


class Commander:

    COMMAND_MOVE = "move"
    COMMAND_EXIT = "exit"

    instance = None

    @staticmethod
    def get_instance():
        if Commander.instance is None:
            Commander.instance = Commander()
        return Commander.instance

    def __init__(self):
        self.arm_motor = ArmMotor.get_instance()

        self.command_map = {
            Commander.COMMAND_MOVE: self.move,
            Commander.COMMAND_EXIT: self.exit,
        }

    def move(self, args):
        self.arm_motor.move_to_position(int(args[0]), int(args[1]))

    @staticmethod
    def exit(args):
        os._exit(0)

    @staticmethod
    def execute(command, debug=False):

        if command not in Commander.get_instance().command_map.keys():
            Commander.help_commands()
            return False
        else:
            func = Commander.get_instance().command_map[command]

            list_tokens = command.split()
            args = list_tokens[1:]

            func(args)

            if debug:
                print("Executed")
            return True

    @staticmethod
    def help_commands():
        print("Command list:")

        for command in Commander.get_instance().command_map.keys():
            print(command)

