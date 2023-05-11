# Jeu-du-pendu
##Contenu du dépôt 
Le dépôt Jeu-du-pendu contient un fichier _mot_pendu.txt_ contenant la liste des mots disponibles pour le jeu ainsi que le script du jeu (.py). 
##Fonctionnement du jeu 
-A l'exécution du script, un mot va être aléatoirement sélectionné dans le fichier txt et la partie commence. Vous avez 6 chances pour trouver le mot sélectionné.
-A chaque erreur, vous perdez une vie. Pour choisir une lettre, il faut directement l'inscrire dans le terminal à la suite du message "Choisissez une lettre : ".
-En cas de saisie d'une lettre déjà proposée, aucune vie n'est enlevée et la liste des lettres restantes est automatiquement affichée. 
-Lorsque qu'une lettre est trouvée, le mot s'affiche avec toutes les lettres trouvées auparavant.

Bon jeu ! 
![Jeu Pendu](data:image/png;base64,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)
