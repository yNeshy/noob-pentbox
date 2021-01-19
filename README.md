# Understanding the topic

### 1. menus:
in the CLIMenus class in cli.py, it's pretty intuitive.

### 2. inputs

    
###    1, il y aura un sous menu :
##### a- Pour la saisie d’un texte et son codage.
##### b- Pour le décodage du message codé.
### 2 : Pour la saisie d’un texte, le choix de la fonction de hachage, puis le calcul du hash.
### 3 : Pour la saisie du hash, choix du dictionnaire de données, craquage du hash.
    
###    4 :
##### a- Saisie du message à chiffrer
    a. Choisir l’algorithme de chiffrement symétrique
    b. Générer le mot de passe (clé symétrique) en mode illisible.
    c. Afficher le message chiffré.
##### b- Saisie du message chiffré
    a. Afficher l’algorithme utilisé le chiffrement symétrique
    b. Saisir son pwd
    c. Afficher le message en clair
    
###    5 :
##### a- Saisie du message à chiffrer
    a. Choisir l’algorithme de chiffrement Asymétrique
    b. Générer les paires de clés.
        i. Protéger sa clé privée par un PWD
    c. Choisir soit chiffrer soit signer le message
    d. Afficher le message chiffré ou bien signé.

##### b- Saisie du message chiffré
    a. Afficher l’algorithme utilisé le chiffrement Asymétrique
    b. Saisir son pwd de protection de sa clé privée
    c. Choisir soit déchiffrer soit vérifier le message
    d. Afficher le message en clair
    
###    6, Quitter.


# noob-pentbox



# Notes:

### Keys are not encrypted when stored
### Private keys SHOULD NOT be stored where they are. This is only for Demo purposes, if this was a real project to be used (or if you intend to make use of this tool) please consider moving the storage of private keys to a remote, safe storage provider.


# Contact
Aziz Nechi
Ghaith Nabli
newghaithofrome@gmail.com
zizou.nechi@gmail.com
