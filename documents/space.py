import pygame  # necessaire pour charger les images et les sons
import random
import math

class Joueur() : # classe pour créer le policier
    def __init__(self) :
        self.position = 600
        self.image = pygame.image.load("policier.png")
        self.sens = "O"
        self.vitesse = 3
        self.score = 0

    def deplacer(self) :
        if (self.sens == "droite") and (self.position < 740):
            self.position = self.position + self.vitesse
        elif (self.sens == "gauche") and (self.position > 0):
            self.position = self.position - self.vitesse
           
    def tirer(self):
        self.sens = "O"
        
    def marquer(self):
        self.score = self.score + 1
    
    def dessiner_score(self, surface):
        font = pygame.font.Font(None, 36)  # Crée une police
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255)) 
        surface.blit(score_text, (10, 760))  # Dessine le texte
    
    def augmenter_vitesse(self):
        self.vitesse += 1

class Donnut() :
    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.position + 16
        self.hauteur = 492
        self.image = pygame.image.load("Donnut.png")
        self.etat = "chargé"
        self.vitesse = 5
    
    def bouger(self):
        if self.etat == "chargé":
            self.depart = self.tireur.position + 16
            self.hauteur = 492
        elif self.etat == "lancée" :
            self.hauteur = self.hauteur - self.vitesse
        
        if self.hauteur < 0:
            self.etat = "chargé"
                
    def toucher(self, vaisseau):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.depart) < 40):
            self.etat = "chargé"
            return True
  
class Ennemi():
    NbEnnemis = 6
    
    def __init__(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if  (self.type == 1):
            self.image = pygame.image.load("1.png")
            self.vitesse = 1
        elif (self.type ==2):
            self.image = pygame.image.load("2.png")
            self.vitesse = 2
            
    def avancer(self):
        self.hauteur = self.hauteur + self.vitesse
    
    def disparaitre(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if  (self.type == 1):
            self.image = pygame.image.load("1.png")
            self.vitesse = 1
        elif (self.type ==2):
            self.image = pygame.image.load("2.png")
            self.vitesse = 2
    
    def augmenter_vitesse(self, joueur_score):
        if joueur_score % 5 == 0:  # Vérifiez si le score du joueur est un multiple de 5
            self.vitesse += 1