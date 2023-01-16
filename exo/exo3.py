"""
## Exigences

* Mettre en avant un principe de classe abstraite
* Mettre en avant un principe de polymorphisme
* Mettre en avant un principe d'héritage multiple
* Max 3 méthodes par classe (hors getter/setter)
* Pas d'algorithmes complexes, juste des print ;)
* En tant que client, je veux pouvoir jouer avec trois types/dérivés de robots différents

### Aide

Sortez un bon vieux crayon pour schématiser vos dépendances d'héritages
"""

""" You can use classes below or create your own 👍️"""

print("PRINCIPE DE CLASSE ABSTRAITE")
	
from abc import ABCMeta,abstractmethod
import time

class UnmannedVehicle(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """
    @abstractmethod
    def debut_mission(self,mission):
        pass

    @abstractmethod
    def fin_mission(self):
        pass

    pass

class AerialVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def debut_vol(self):
        pass

    @abstractmethod
    def looping(self):
        pass

    @abstractmethod
    def fin_vol(self):
        pass

    pass

class GroundVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""

    @abstractmethod
    def mise_en_marche(self):
        pass
    
    @abstractmethod
    def arret(self):
        pass
    pass

class UnderseaVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""

    @abstractmethod
    def plonger(self):
        pass

    def duree(self):
        print("temps pouvant rester sous l'eau")
        time.sleep(5)
        self.sorti()
        self.plonger()
        pass

    @abstractmethod
    def sorti(self):
        pass

    pass

class UAV(UnmannedVehicle,AerialVehicle):
    
    def debut_vol(self):
        print("UAV vole")

    def looping(self):
        print("UAV looping")

    def fin_vol(self):
        print("UAV à terre")

    def debut_mission(self, mission):
        print('Début de mission :', mission)
        self.debut_vol()
        self.looping()

    def fin_mission(self):
        print('Fin de mission')
        self.fin_vol()

class UUV(UnmannedVehicle,UnderseaVehicle):
    
    def plonger(self):
        print("UUV en plongé")
    
    def sorti(self):
        print("UUV sorti")

    def debut_mission(self, mission):
        print('Début de mission :', mission)
        self.plonger()
        self.duree()

    def fin_mission(self):
        print('Fin de mission')
        self.sorti()

class UGV(UnmannedVehicle,GroundVehicle):

    def mise_en_marche(self):
        print("UGV en marche")
    
    def arret(self):
        print("UGV en arrêt")

    def debut_mission(self, mission):
        print('Début de mission :', mission)
        self.mise_en_marche()

    def fin_mission(self):
        print('Fin de mission')
        self.arret()


if __name__ == '__main__':
    uav = UAV()
    uav.debut_mission("Détection des principaux ennemis sur le terrain:Adrien, Coline, Le Rouquin, Marie")
    uav.fin_mission()
    print()

    ugv = UGV()
    ugv.debut_mission("transport de 100 millions de scies commandés par Florian")
    ugv.fin_mission()
    print()

    uuv = UUV()
    uuv.debut_mission("Exploration sous-marine effectué par Lola et ses chats")
    uuv.fin_mission()
    print()
