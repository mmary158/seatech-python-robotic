"""
* Réutiliser la class Robot faite dans l'exo 1. *Sans copier/coller dans le fichier ;)*
* Un humain doit posséder un sexe attribuable à  sa création
* Un humain doit pouvoir manger un ou plusieurs aliments
* Un humain doit pouvoir digérer ce qu'il a mangé *pas très important, faire en dernier si vous avez le temps
* Un Cyborg doit être une combinaison d'un humain et d'un robot
* Bonus : ajouter une méthode fun au Cyborg
"""
import time
from exo1 import Robot

class Human():   
    sexe=None
    estoma=[]
    
    def __init__(self,sexe):
        if sexe:
            self.sexe=sexe
    
    def eat(self,aliment):
        self.estoma.append(aliment)
        print("aliment mangé:%s"%(self.estoma))
    
    def digest(self):
        while self.estoma!=[]:
            a=self.estoma[0]
            if a!=[]:
                self.estoma.remove(a)
                print("aliment digéré:%s"%(a))
            time.sleep(4)
            



class Cyborg(Robot,Human):
    courir=False
    obstacleface=False
    obstacledroite=False
    obstaclegauche=False
    saut=False

    def __init__(self,name,sexe):
        if name:   
            Robot.__init__(self,name)
            Human.__init__(self,sexe)

    def parcours(self):
        self.courir=True
        if self.obstacleface==True:
            if self.obstacledroite==True and self.obstaclegauche==True:
                



    

if __name__=='__main__':
    cyborg = Cyborg('Deux Ex Machina','M')
    cyborg.etat()
    print("sexe:%s"%(cyborg.sexe))
   # cyborg.charge()
    cyborg.eat('Lola')
    cyborg.eat('chocolatine')
    cyborg.eat('chat')
    cyborg.eat('chien')
    cyborg.eat('hamster')
    cyborg.digest()

    