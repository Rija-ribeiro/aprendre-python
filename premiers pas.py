# bonjour, nous allons ici découvrire les principales bases de pyton.
# tout dabord vous pouvez télécharger (si vous n'en avez pas déja un l'IDLE edupython:
# http://download.tuxfamily.org/edupython/Setup_EP27.exe


### LES COMMENTAIRES ###################################################################################################
# les comentaire en python servent à écrire des chose pour mieux
#   comprendre son programme sans que l'ordinateur s'en préocupe.
# pour écrire un commentaire, on ajoute donc # au début de la ligne.


### LA FONCTION PRINT ##################################################################################################
# pour demander à l'ordinateur de dire quelque chose nous pouvons executer la commende suivante:
print("votre texte")
#>>> votre text
print("votre texte"+" mon text")
#>>> votre text mon text
print("cou"*2)
#>>> coucou
print("1"+"3")
#>>> 13
print(1)
#>>> 1
print(1+3)
#>>> 3
print(3*2)
#>>> 6
# pour du texte, les guillemets sont obligatoire.


### LES OPÉRATEURS LOGIQUES ############################################################################################
# +   : addition
# -   : soustraction
# *   : multiplication
# /   : division
# **  : puissance
# %   : reste de la division euclidienne

### LES TYPES DE DONÉE #################################################################################################
# en python il existe diférent types de donnée:
# les textes  : "text"                  => doivent être entre guillemets.
# les nombres : 0123456789              => s'écrivent juste avec des nombre normaux.
# les liste   : [élément1,element2,...] => doivent être entre crochet, et chaque éléments séparé pa une virgule.
# les tuples  : (élément1,element2,...) => se comportent comme des liste mais ne sont pas modifiable par la suite

# pour avoir l'élément x d'une liste ou d'un tuple, on note la_liste[x]
print(["bonsoir","bonjour","bonne journée"][1]) # /!\ le premier élément c'est l'élément 0. L'élément 1 c'est donc le deuxième.
#>>> bonjour

# pour avoir l'élément avant l'élément x d'une liste ou d'un tuple (élément x exclus), on note la_liste[:x]
print(["bonsoir","bonjour","bonne journée"][:2])
#>>> bonsoirbonjour

# pour avoir l'élément après l'élément x d'une liste ou d'un tuple (élément x inclus), on note la_liste[:x]
print(["bonsoir","bonjour","bonne journée"][1:])
#>>> bonjourbonne journée

print(["rien"]*2)
#>>> ["rien","rien"]

print(["rien"]+["rien"]*2)
#>>> ["rien","rien"]

# pour transformer une donnée en un autre type il existe plusieur comande:
# str(donnée)   : transforme en texte
# int(donnée)   : transforme en nombre entier
# float(donnée) : transforme en nombre à virgule
# list(donnée)  : transforme en liste
# tuple(donnée) : transforme en tuple

print(str(1)+" chat")
#>>> 1 chat

print(int("1.3")+1)
#>>> 2

print(float("1.3")+1)
#>>> 2.3


### LES VARIABLES ######################################################################################################
# en python, la création et l'atribution des variables se fait en même temps.
nom_de_variable = "tu texte"
nom_de_variable = 1 # un nombre
nom_de_variable = ["bonjour","salut",1,"bienvenu"] # une liste
nom_de_variable = ("chaton",4,"moustique") # un tuple
print(nom_de_variable)
#>>> ("chaton",4,"moustique")

# on peut ajouter quelque chose à une variable en faisant
nom_de_variable += ("rat")
print(nom_de_variable)
#>>> ("chaton",4,"moustique","rat")

# ou en faisant
nom_de_variable = nom_de_variable+"rat"

# ou la multiplier
nom_de_variable *= 2

# si la variable contient une liste on peut suprimer l'élément x,tout ceux avant et tout ceux après en faisant
print(nom_de_variable)
#>>> ("chaton",4,"moustique","rat","rat","chaton",4,"moustique","rat","rat")

del(nom_de_variable[2])
print(nom_de_variable)
#>>> ("chaton",4,"rat","rat","chaton",4,"moustique","rat","rat")

del(nom_de_variable[:2])
print(nom_de_variable)
#>>> ("rat","rat","chaton",4,"moustique","rat","rat")

del(nom_de_variable[4:])
print(nom_de_variable)
#>>> ("rat","rat","chaton",4,)

#ÉCRIS MOI QUAND TU AS FINIS ET SI TU AS UN PROBLÈME? TOUTES LES INFOS SONT DANS README.md
