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
        self.clifffrontleft=DistanceSensor("cliff_front_left")
        self.clifffrontright=DistanceSensor("cliff_front_right")
        self.cliffleft=DistanceSensor("cliff_left")
        self.cliffright=DistanceSensor("cliff_right")

    def bump(self): # détecter si on a foncer dans un obstacle
        print(self.bumperleft.BUMPER)
        if self.bumperleft.BUMPER==1 or self.bumperright.BUMPER==1:
            self.vitesse=-self.vitesse
            #print(self.bumperleft.BUMPER)

    def distance(self): #détecter la présence d'un objet
        print(self.cliffright)
        

    def run(self):
        self.__leftMotor.setVelocity(16)
        self.__rightMotor.setVelocity(16)
        #self.bump()
        self.distance()
  

                    
        
# create the Robot instance.
robot = SeatechRobot()
while robot.step(TIME_STEP) != -1:
    robot.run()
   