import re
nom_de_fichier = "Advent of coding\\2023\j1.in"

# Partie 1
sum = 0
with open(nom_de_fichier, "r") as f:

    for ligne in f:
        # Explication du Regex [^0-9] en bas du document
        chiffres=re.sub("[^0-9]","",ligne)
        calibration_value = 10*int(chiffres[0])+int(chiffres[-1])
        sum += calibration_value

print(sum)
"""
L'expression régulière [^0-9] est une classe de caractères qui correspond à n'importe quel caractère unique qui n'est pas un chiffre. Voici une explication détaillée :

^ : Dans ce contexte, il est utilisé comme un opérateur de négation à l'intérieur de la classe de caractères. Il nie la classe de caractères, ce qui signifie qu'il correspond à n'importe quel caractère qui n'est pas spécifié entre les crochets.
0-9 : Cette plage représente tous les chiffres de 0 à 9.
"""
#############################################################################################
# Partie 2
sum=0
nombres=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
regex = r'(?=([0-9]|'+ "|".join(n for n in nombres) + r'))'
# regex = (?=([0-9]|one|two|three|four|five|six|seven|eight|nine))
pattern = re.compile(regex) #utile de ne compiler le RegEx qu'une seule fois

with open(nom_de_fichier, "r") as f:
    for ligne in f:
        matches = list(pattern.findall(ligne))
        calibration_value=0

        i=1 # i=1 => dizaine, i=0 => unité
        #pour le premier et le dernier matching
        for m in [matches[0],matches[-1]]:
            if m in nombres:
                m = nombres.index(m) + 1
            else:
                m = int(m)
            calibration_value += m*(10**i)
            i -= 1
        sum += calibration_value

print(sum)


"""
Le regex (?=([0-9]|one|two|three|four|five|six|seven|eight|nine)) utilise une assertion positive (?= ...) 
Voici une explication détaillée :
(?= ...) signifie que la correspondance doit être suivie par ce qui est à l'intérieur de la parenthèse sans consommer ces caractères dans la correspondance principale.
"""