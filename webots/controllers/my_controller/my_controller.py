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
    def __init__(self):
        super().__init__()
        self.vitesse=16.129
        self.__leftMotor = RobotMotor('left wheel motor')
        self.__rightMotor = RobotMotor('right wheel motor')
        self.bumperleft=TouchSensor("bumper_left")
        self.bumperright=TouchSensor("bumper_right")


    def bump(self): # détecter si on a foncer dans un obstacle
        if self.bumperleft.getValue()>0 or self.bumperright.getValue()>0:
            self.vitesse=-self.vitesse
    
    def toutdroit(self,vitesse):
        self.__leftMotor.setVelocity(vitesse)
        self.__rightMotor.setVelocity(vitesse)
            
    def run(self):
        self.toutdroit(self.vitesse)
        self.bump()
        
        
# create the Robot instance.
robot = SeatechRobot()
while robot.step(TIME_STEP) != -1:
    robot.run()
   