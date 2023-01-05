class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    time=0
    __states = ['shutown', 'running']
    
        
    """
      Give your best code here ( •̀ ω •́ )✧
    """
    def __init__(self,name=None,power=False,current_speed=0,battery_level=0,states=[]):
        if name:
            self.__name=name
            self.__power=False
            self.__current_speed=self.__current_speed
            self.__battery_level=self.__battery_level
            self.__states=self.__states[0]
    	
    def onoff(self):
      if self.__power==False:self.__power=True
      if self.__power==True:self.__power=False
      print("Le Robot est %s" %(self.__states[self.__power]))
      pass

    def charge(self):
      if self.__battery_level==0:
        while self.time<10:self.__battery_level+=10  
      print("La batterie est chargé à %s"%(self.battery_level))
      pass
