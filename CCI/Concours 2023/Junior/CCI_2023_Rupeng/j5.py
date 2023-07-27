#---------plan---------
#identifier la première lettre du mot et repérer toutes ses occurences dans la grille. enregister la coordonnée dans la liste «amorce»
#en partant de chaque amorce, approfondir la recherche dans toutes les directions linéaires, puis diagonales
#après avoir posé la deuxième lettre, il sera possible de lancer la recherche dans une direction perpendiculaire

DIRECTIONL = [(0, 1), (-1, 0), (1, 0), (0, -1)] #coordonées cartésiennes pour un déplacement linéaire
DIRECTIOND = [(-1, 1), (1, 1), (-1, -1), (1, -1)] #coordonées cartésiennes pour un déplacement diagonal

mot = list(input())
r = int(input())
c = int(input())
longueur, occurence = len(mot), 0

#enregistrer la grille à l'aide des listes emboitées
grille = []
for _ in range(r):
    grille.append(input().split(" "))

#repéter toutes les amorces dans la grille
amorces = []
for i in range(r):
    for j in range(c):
        if grille[i][j] == mot[0]:
            amorces.append((i, j))

def déplacer(origr, origc, dr, dc):
    """
    Cette fonction prend en argument les paramètres de la position originale et la direction du déplacement
    Elle calcule la nouvelle position suite au déplacement
    Retourner False si la nouvelle position est hors limite
    """
    # Calcul des nouvelles coordonnées en soustrayant les déplacements
    y = origr - dr
    x = origc + dc

    # Vérification des limites des coordonnées
    if y < 0 or x < 0 or y >= r or x >= c:
        return False # Si les nouvelles coordonnées sont hors limites, retourne False

    return y, x

def rechercher(r, c, dr, dc, profondeur, direction, pivotant=False):
    """
    Cette fonction permet de continuer la recherche dans une certaine direction (dr, dc) jusqu'à ce qu'on retrouve le mot entier ou jusqu'à
    ce que la chaine se brise.
    Cette fonction permet de relancer la recherche dans une direction perpendiculaire si pivotant=True
    """
    global occurence
    while grille[r][c] == mot[profondeur]:
        profondeur += 1

        #le mot a été retrouvé dans la grille
        if profondeur == longueur:
            occurence += 1
            break
        
        if pivotant and profondeur>1: #il ne sera possible de pivoter qu'après avoir posé les deux premières lettres
            for dc1, dr1 in direction: #s'il est permis de pivoter, lancer la recherche dans une autre direction
                if dc1 == dc and dr1 == dr:continue

                nouvelle_pos = déplacer(r, c, dr1, dc1) #calculer la prochaine case à explorer après avoir pivoté de 90deg
                if not nouvelle_pos:continue #si la nouvelle position est hors limite, sauter à la prochaine direction

                #continuer la recherche en suivant cette direction, sans possibilité de pivoter
                rechercher(*nouvelle_pos, dr1, dc1, profondeur, None, pivotant=False) 
        
        nouvelle_pos = déplacer(r, c, dr, dc)
        if not nouvelle_pos:break
        r, c = nouvelle_pos

#en partant de chaque amorce, approfondir la recherche dans toutes les directions linéaires, puis diagonales
for direction in (DIRECTIONL, DIRECTIOND):
    for amorce in amorces: #pour chaque amorce, explorer en suivant la direction donnée
        for dc, dr in direction:
            rechercher(*amorce, dr, dc, 0, direction, pivotant=True) #lancer la recherche

print(occurence)