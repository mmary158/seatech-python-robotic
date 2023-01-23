from controller import Robot,Motor,DistanceSensor,TouchSensor

TIME_STEP = 64

            
class RobotMotor(Motor):
    def __init__(self, name):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)
        self.max_speed = self.getMaxVelocity()


class SeatechRobot(Robot):
    max_speed=16
    def __init__(self):
        super().__init__()
        self.__leftMotor = RobotMotor('left wheel motor')
        self.__rightMotor = RobotMotor('right wheel motor')
        self.__leftbumper=TouchSensor('bumper_left')
        self.__rightbumper=TouchSensor('bumper_right')
        
    def bump(self):
        self.max_speed=-(self.max_speed)       
        if self.__leftbumper==1:
           self.max_speed=-(self.max_speed) 
        if self.__rightbumper==1:
            self.max_speed=-(self.max_speed)

    
    def run(self):
        self.__leftMotor.setVelocity(self.max_speed)
        self.__rightMotor.setVelocity(self.max_speed)
        self.bump()
  

                    
        
# create the Robot instance.
robot = SeatechRobot()
while robot.step(TIME_STEP) != -1:
    robot.run()
   
