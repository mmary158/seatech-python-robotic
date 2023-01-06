import time
"""
    Lorsque je crée mon robot, je veux pouvoir lui attribuer un nom
    Mon robot doit pouvoir s'allumer
    Mon robot doit pouvoir s'éteindre
    Mon robot doit pouvoir charger sa batterie à 100%, allumé ou non
    Le temps de charge ne peut pas être immédiat (10s max)
    Mon robot doit afficher sont % de batterie durant sa charge
    Mon robot doit pouvoir enregistrer une vitesse de déplacement
    Mon robot doit pouvoir me donner sa vitesse de déplacement
    Mon robot doit pouvoir arrêter son déplacement sur commande
    Mon robot doit pouvoir me fournir un résumé de son état global
"""
class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutdown', 'running']

    def __init__(self,name):
        if name:
            self.__name=name
            self.__power=Robot.__power
            self.__current_speed=Robot.__current_speed
            self.__battery_level=Robot.__battery_level
    	
    def on(self):
      self.__power=True
      self.current_status=self.__states[1]
      print("Le Robot est %s" %(self.current_status))
    
    def off(self):
      self.__power=False
      self.current_status=self.__states[0]
      print("Le Robot est %s" %(self.current_status))
  
    def charge(self):
      while self.__battery_level<100:
          self.__battery_level+=10  
          print("La batterie est chargé à %s"%(self.__battery_level),"%")
          time.sleep(1)

    def infovitesse(self):
      self.enregistrement=self.__current_speed
      print("Le robot a une vitesse de déplacement de %s"%(self.__current_speed),"km/h")

    def arret(self):
      self.__current_speed=0

    def etat(self):
      print("%s"%(self.__name))
      print("Robot %s"%(self.current_status))
      print("vitesse de déplacement:%s"%(self.__current_speed),"km/h")
      print("Batterie chargé:%s"%(self.__battery_level),"%")

    def vitesse(self,speed):
      if self.current_status==self.__states[1]:
        self.__current_speed=speed

"""
robot=Robot(name="Wall-E")
robot.on()
robot.etat()

"""





