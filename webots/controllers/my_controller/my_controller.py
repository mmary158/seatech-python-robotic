from controller import Robot,Motor,DistanceSensor,TouchSensor,GPS
import time

TIME_STEP = 64

"""
 class myGPS(GPS):

    def __init__(self):
        super().__init__("mongps")

    def my_fonction():
        pass
"""

class RobotMotor(Motor):
    def __init__(self, name):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)
        self.max_speed = self.getMaxVelocity()

class SeatechRobot(Robot):
    vitesse=0
    def __init__(self):
        self.vitesse=16.129
        super().__init__()
        self.__leftMotor = RobotMotor('left wheel motor')
        self.__rightMotor = RobotMotor('right wheel motor')
        self.bumperleft=TouchSensor("bumper_left")
        self.bumperright=TouchSensor("bumper_right")

    def bump(self): # détecter si on a foncer dans un obstacle
        if self.bumperleft.getValue()==1 or self.bumperright.getValue()==1:
            self.vitesse=-self.vitesse
            print("a bumpe")
            
    def run(self):
        self.__leftMotor.setVelocity(self.vitesse)
        self.__rightMotor.setVelocity(self.vitesse)
        self.bump()
        
        
# create the Robot instance.
robot = SeatechRobot()
while robot.step(TIME_STEP) != -1:
    robot.run()
   