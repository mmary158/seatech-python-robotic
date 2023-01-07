"""
* RÃ©utiliser la class Robot faite dans l'exo 1. *Sans copier/coller dans le fichier ;)*
* Un humain doit posséder un sexe attribuable à  sa création
* Un humain doit pouvoir manger un ou plusieurs aliments
* Un humain doit pouvoir digérer ce qu'il a mangé *pas très important, faire en dernier si vous avez le temps
* Un Cyborg doit être une combinaison d'un humain et d'un robot
* Bonus : ajouter une méthode fun au Cyborg
"""
from exo1 import Robot

# class Robot():
#      #Robot class content here
#     pass

class Human():   
    sexe=None
    estomavide=False
    estoma=[]
    
    def __init_(self,sexe):
        if sexe:
            self.sexe=sexe
    
    def eat(self,aliment):
        if self.estomavide==True:
            self.estoma.append(aliment)
            self.digest()
    
    def digest(self):
        #4 h dans l'estomac 
        # 4h intestin grêle
        # 16h dans le gros intestin
        
        
class Cyborg(Robot, Human):
    name="<unnamed>"   
    sexe="<unnamed>"
    def __init__(self,name,sexe):
        if name:   
            Robot.__init__(self,name)
            Human.__init__(self,sexe)

"""
cyborg = Cyborg('Deux Ex Machina','M')

print(cyborg.name, 'sexe', cyborg.sexe)

print('Charging battery...')
cyborg.charge()
cyborg.status()
cyborg.eat('banana')
cyborg.eat(['coca', 'chips'])
cyborg.digest()
"""