from commanders.Commander import Commander


class KeyboardCommander:

    last_command = None

    @staticmethod
    def start():

        while True:
            command = input("Insert command: ")
            last_command = KeyboardCommander.last_command

            if command == "r" and last_command is not None:
                Commander.execute(last_command)
            else:
                Commander.execute(command)
                KeyboardCommander.last_command = command

