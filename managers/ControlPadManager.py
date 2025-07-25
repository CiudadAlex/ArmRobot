from actuators.ArmMotor import ArmMotor
import time
import ipywidgets.widgets as widgets


class ControlPadManager:

    def __init__(self):

        self.controller = widgets.Controller(index=0)
        self.arm_motor = ArmMotor()

    def start_control(self):

        while 1:
            self.check_controller_and_move_arm()

    def check_controller_and_move_arm(self):

        # Due to individual differences in joystick handles, all joystick reset values are not necessarily zero,
        # so 0.1 needs to be used as a filter to avoid misoperation.

        # Servo No. 2, A1 is negative up and down positive
        if 0.1 >= self.controller.axes[1].value >= -0.1:
            time.sleep(.000001)
        else:
            more_or_less = self.controller.axes[1].value > 0.1
            self.arm_motor.move(2, more_or_less)

        # Servo No. 1, A0 left negative and right positive
        if 0.1 >= self.controller.axes[0].value >= -0.1:
            time.sleep(.000001)
        else:
            more_or_less = self.controller.axes[0].value <= 0.1
            self.arm_motor.move(1, more_or_less)

        # Servo No. 6, NUM1=B0, NUM3=B2, A2 is up negative and down is positive
        if self.controller.buttons[0].value:
            self.arm_motor.move(6, True)
        elif self.controller.buttons[2].value:
            self.arm_motor.move(6, False)
        elif self.controller.axes[2].value > 0.5:
            self.arm_motor.move(6, False)
        elif self.controller.axes[2].value < -0.5:
            self.arm_motor.move(6, True)

        # Servo No. 5, NUM2=B1, NUM4=B3, A5 is negative on the left and positive on the right
        if self.controller.buttons[1].value:
            self.arm_motor.move(5, True)
        elif self.controller.buttons[3].value:
            self.arm_motor.move(5, False)
        elif self.controller.axes[5].value > 0.5:
            self.arm_motor.move(5, True)
        elif self.controller.axes[5].value < -0.5:
            self.arm_motor.move(5, False)

        # Servo No. 4，R1=B5,R2=B7
        if self.controller.buttons[5].value:
            self.arm_motor.move(4, False)
        elif self.controller.buttons[7].value:
            self.arm_motor.move(4, True)

        # Servo No. 3，L1=B4,L2=B6
        if self.controller.buttons[4].value:
            self.arm_motor.move(3, False)
        elif self.controller.buttons[6].value:
            self.arm_motor.move(3, True)

        # Press the selection button B8 to set the servos of the robotic arm to 90 degrees
        if self.controller.buttons[8].value:
            self.arm_motor.home()

