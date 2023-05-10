import random

#FONCTION D'IMPORTATION D'UN MOT
def choix_mot ():
    with open("mots_pendu.txt", 'r') as f:
        liste_mots = list(map(str, f.read().split()))                 
        return random.choice(liste_mots)
        
print(choix_mot())
