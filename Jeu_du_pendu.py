'''Le code suivant est une application du jeu du pendu. Se référer au document README afin de comprendre le fonctionneemnt'''

import random
import string

#FONCTION D'IMPORTATION D'UN MOT CHOISI ALEATOIREMENT DANS LE FICHIER 'mots-pendu.txt'
def choix_mot ():
    with open("mots_pendu.txt", 'r') as f:
        liste_mots = list(map(str, f.read().split()))                 
        return random.choice(liste_mots)
    
#FONCTION QUI TEST SI LA LETTRE CHOISIE EST DANS LE MOT (return true si c'est le cas)
def lettre_trouve (mot, lettre): 
    if mot.count(lettre) !=0 : 
        return True 
    else: 
        return False

#FONCTION POUR AFFICHER LE MOT 
def afficher_mot(mot):
    for i in mot :
        print(i,end=" ") 
    print("\n")
        
#PROCEDURE DE JEU 
def jeu_pendu (mot):
    print('Bienvenue dans le jeu du pendu. Tu as 6 chances pour trouver le mot')
    vie = 6 
    win = False 
    mot_trouve=[]
    
    for i in mot: #INITIALISATION de l'alphabet et de mot_trouve
        mot_trouve+=["__"]
    alphabet_restant = list(string.ascii_lowercase)
    
    while vie > 0 and not win :
        lettre = (input("Choisissez une lettre : "))    
        if alphabet_restant.count(lettre) == 0 :  #La lettre a déjà été séléctionné 
            print('La lettre a déjà été choisie, rééssayer avec une des lettres restantes : ')
            afficher_mot(alphabet_restant)    
        else: 
            alphabet_restant.remove(lettre)
            if lettre_trouve(mot, lettre) : #La lettre est dans le mot
                for i in range(0,len(mot)): 
                    if mot[i]==lettre: 
                        mot_trouve[i]=lettre    
                print(f"La lettre {lettre} est dans le mot. {vie} vie(s) restante(s)")
                afficher_mot(mot_trouve)
                if mot_trouve.count('__')==0:
                    win=True
            else: #La lettre n'est pas dans le mot                
                vie-=1
                print(f"La lettre {lettre} n'est pas dans le mot, {vie} vie(s) restante(s)")
                                
    if vie <= 0 : #Vie épuisée
        print(f"Perdu, le mot était {mot}, recommence")
    else : #Victoire
        print(f"Bravo, le mot était bien {mot}, CHAMPION")                   
    
#CORPS DU PROGRAMME
jeu_pendu(choix_mot())