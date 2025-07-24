from actuators.ArmMotor import ArmMotor
import time

arm_motor = ArmMotor()

 def Arm_Handle():
    s_time = 500
    s_step = 1
    angle_1 = angle_2 = angle_3 = angle_4   =  angle_5 = angle_6 = 90
    while 1:
        #Due to individual differences in joystick handles, all joystick reset values are not necessarily zero, so 0.1 needs to be used as a filter to avoid misoperation.
        # Servo No. 2, A1 is negative up and down positive
        if controller.axes[1].value <= 0.1   and controller.axes[1].value >= -0.1:
            time.sleep(.000001)
        else:
            if controller.axes[1].value >   0.1:
                angle_2 += s_step
            else:
                angle_2 -= s_step
            arm_motor.move(2, more_or_less)
        # Servo No. 1, A0 left negative and right positive
        if (controller.axes[0].value <=   0.1 and controller.axes[0].value >= -0.1):
                time.sleep(.000001)
        else:
            if controller.axes[0].value >   0.1:
                angle_1 -= s_step
            else:
                angle_1 += s_step
            arm_motor.move(1, more_or_less)
        # Servo No. 6, NUM1=B0, NUM3=B2, A2 is up negative and down is positive
        if controller.buttons[0].value ==   True:
            angle_6 += s_step
            arm_motor.move(6, more_or_less)
        elif controller.buttons[2].value ==   True:
            angle_6 -= s_step
            arm_motor.move(6, more_or_less)
        elif controller.axes[2].value >   0.5:
            angle_6 -= s_step
            arm_motor.move(6, more_or_less)
        elif controller.axes[2].value <   -0.5:
            angle_6 += s_step
            arm_motor.move(6, more_or_less)
        # Servo No. 5, NUM2=B1, NUM4=B3, A5 is negative on the left and positive on the right
        if controller.buttons[1].value ==   True:
            angle_5 += s_step
            arm_motor.move(5, more_or_less)
        elif controller.buttons[3].value ==   True:
            angle_5 -= s_step
            arm_motor.move(5, more_or_less)
        elif controller.axes[5].value >   0.5:
            angle_5 += s_step
            arm_motor.move(5, more_or_less)
        elif controller.axes[5].value <   -0.5:
            angle_5 -= s_step
            arm_motor.move(5, more_or_less)
        # Servo No. 4，R1=B5,R2=B7
        if controller.buttons[5].value ==   True:
            angle_4 -= s_step
            arm_motor.move(4, more_or_less)
        elif controller.buttons[7].value ==   True:
            angle_4 += s_step
            arm_motor.move(4, more_or_less)
        # Servo No. 3，L1=B4,L2=B6
        if controller.buttons[4].value == True:
            angle_3 -= s_step
            arm_motor.move(3, more_or_less)
        elif controller.buttons[6].value ==   True:
            angle_3 += s_step
            arm_motor.move(3, more_or_less)
        # Press the selection button B8 to set the servos of the robotic arm to 90 degrees
        if controller.buttons[8].value ==   True:
            angle_1 = angle_2 = angle_3 =   angle_4 = angle_5 = angle_6 = 90
            arm_motor.home()
