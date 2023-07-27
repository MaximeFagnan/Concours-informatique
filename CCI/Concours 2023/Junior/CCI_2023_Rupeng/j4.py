#---------plan---------
#commencer par calculer le périmètre en multipliant le nb de triangles par 3
#calculer le nb de côtés adjacents sur...
#   une même rangée
#   une même colonne
#soustraire à du périmètre 2x le nb de côtés adjacents de manière à enlever les limites si les deux triangles se touchent

col = int(input()) #nb de colonnes

#les listes ran1 1 et ran2 représentent l'état des tuiles
#True si la case est noire et False si elle est blanche
ran1 = [i=="1" for i in input().split(" ")]
ran2 = [i=="1" for i in input().split(" ")]
périmètre = (sum(ran1) + sum(ran2))*3 #périmètre avant ajustement

#nombre de côtés adjacents sur une même rangée
#ran1[:-1] donne toutes les éléments dans la liste sauf le dernier
#la fonction zip assemble les deux valeurs de tuile sur une même colonne dans un même tuple (ex:[True, False])
for i, (tuile1, tuile2) in enumerate(zip(ran1[:-1], ran2[:-1])):
    périmètre -= 2*int(tuile1 and ran1[i+1]) #-2 si la tuile 1 et la prochaine sur la rangée sont noires
    périmètre -= 2*int(tuile2 and ran2[i+1]) #-2 si la tuile 2 et la prochaine sur la rangée sont noires
    
    #la base des triangles sont du même côté pour une colonne sur deux
    #les colonnes 0, 2, 4, ... contiennent deux triangles dont les bases sont alignés
    if not i%2:
        périmètre -= 2*int(tuile1 and tuile2) #-2 si les deux tuiles sur la même colonne sont noires

#vérifier si les deux triangles sont peinturés sur la dernière colonne
if col%2 and bool(ran1[-1] and ran2[-1]):
    périmètre -= 2

print(périmètre)


"""
Notons qu'aux lignes 20 et 21, il est possible de rendre la recherche des triangles adjacents plus efficace en créant une variable
qui enregistre l'état de coloration de la tuile précédante. Cette valeur est ensuite comparée à la tuile présente.
D'une telle manière, on ne lit la valeur de chaque tuile qu'une seule fois. Par contre, l'implémentation de cette algorithme 
sera un peu plus longue. 
"""