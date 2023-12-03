import re
nom_de_fichier = "Advent of coding\\2023\j2.in"

# Partie 1
sum = 0
with open(nom_de_fichier, "r") as f:

    for parties in f:
        partie = re.split("Game |: ", parties)
        partie.pop(0) #le regex créer une chaîne de caractère vide en partie[0]
        numero_de_partie = int(partie.pop(0))
        #partie[0] contient tout les rondes
        rondes = partie[0].split("; ")

        partie_valide = True
        for ronde in rondes:
            pige = ronde.split(",")
            for num_et_couleur in pige:
                num, couleur = num_et_couleur.split()
                num = int(num)
                if couleur == "red" and num>12:
                    partie_valide = False
                if couleur == "green" and num>13:
                    partie_valide = False
                if couleur == "blue" and num>14:
                    partie_valide = False

        if partie_valide:
            sum += numero_de_partie

print(sum)
#############################################################################################

# Partie 2
sum=0

with open(nom_de_fichier, "r") as f:

    for parties in f:
        partie = re.split("Game |: ", parties)
        partie.pop(0) #le regex créer une chaîne de caractère vide en partie[0]
        numero_de_partie = int(partie.pop(0))
        #partie[0] contient tout les rondes
        rondes = partie[0].split("; ")

        min_red = 0
        min_green = 0
        min_blue = 0
        for ronde in rondes:
            pige = ronde.split(",")
            for num_et_couleur in pige:
                num, couleur = num_et_couleur.split()
                num = int(num)
                if couleur == "red" and num>min_red:
                    min_red = num
                if couleur == "blue" and num>min_blue:
                    min_blue = num
                if couleur == "green" and num>min_green:
                    min_green = num
        print(min_red,min_blue,min_green)
        puissance = min_red * min_green * min_blue
        print(puissance)
        sum += puissance
print(sum)