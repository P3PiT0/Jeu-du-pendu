import random
import string

#FONCTION D'IMPORTATION D'UN MOT
def choix_mot ():
    with open("mots_pendu.txt", 'r') as f:
        liste_mots = list(map(str, f.read().split()))                 
        return random.choice(liste_mots)
        
#PROCEDURE DE JEU 
def jeu_pendu (mot):
    vie = 6 
    win = False
    #mot_trouve
    alphabet_restant = list(string.ascii_lowercase)
    while vie > 0 and not win : 
        lettre = (input("Choisissez une lettre : "))    
        if alphabet_restant.count(lettre) == 0 : 
            print('La lettre a déjà été choisi, rééssayer avec une des lettres restantes : ')
            print(alphabet_restant)
            
        else: 
            alphabet_restant.remove(lettre)

            '''for i in mot: 
                if lettre == i : 
                    #CAS 1 toutes lettres trouvée 
                    #CAS 2 reste une lettre a trouver '''
                        
    
#CORPS DU PROGRAMME
jeu_pendu(choix_mot())
