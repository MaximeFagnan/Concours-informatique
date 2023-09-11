"""---------plan---------
!!! L'ordre des coups de pinceau importe peu
1. Compter le nombre de cases dorées après l'application des coups de pinceau sur les rangées
2. Additionner ce nombre aux nombres au nombre de cases dorées après l'application des coups de pinceau sur les colonnes
3. Soustraire le nombre de cases comptés en surplus"""

m = int(input())
n = int(input())
k = int(input())

# enregistrer les opérations sur les rangées et colonnes
# True si opération appliquée un nombre impair de fois, sinon, False
r, c = [False]*m, [False]*n

for _ in range(k):
    orientation, ligne = input().split(" ")
    ligne = int(ligne)

    #opérateur XOR inverse la valeur
    if orientation == "R":r[ligne-1] ^= True
    else:c[ligne-1] ^= True

r = sum(r)
c = sum(c)

n_dorée = r*n + c*m - 2*r*c
print(n_dorée)