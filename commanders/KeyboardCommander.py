from commanders.Commander import Commander


class KeyboardCommander:

    @staticmethod
    def start():

        while True:
            command = input("Insert command: ")
            Commander.execute(command)

