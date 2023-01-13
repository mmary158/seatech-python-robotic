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
	
from abc import ABCMeta
from abc import abstractmethod

class UnmannedVehicle(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """
    pass

class AerialVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    pass

class GroundVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    pass

class UnderseaVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    pass

class UAV():
    
    def do_something_interesting(self):
        pass
    def do_something_aerial_specific(self):
        pass

class UUV():
    def do_something_interesting(self):
        pass
    def do_something_undersea_specific(self):
        pass

class UGV():
    def do_something_interesting(self):
        pass
    def do_something_ground_specific(self):
        pass


if __name__ == '__main__':
    uav = UAV()
    uav.do_something_interesting()
    uav.do_something_aerial_specific()

    ugv = UGV()
    ugv.do_something_interesting()
    ugv.do_something_ground_specific()

    uuv = UUV()
    uuv.do_something_interesting()
    uuv.do_something_undersea_specific()
