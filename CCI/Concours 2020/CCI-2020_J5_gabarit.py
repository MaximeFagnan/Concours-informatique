M=3  #à modifier plus tard pour prendre le input et le transformer en entier
N=4  #à modifier plus tard pour prendre le input et le transformer en entier

# Notons que grille[0][j] et grille[i][0] seront 0 pour notre convénience
grille = [[0]*(M+1) for i in range(N+1)]
# pour accéder à l'élément en position (i,j) grille[i][j]

# La grille devrait ressembler à ceci lorsqu'on a terminé (supprimer ces lignes après les tests)
grille = [[0,0,0,0,0], [0, 3, 10, 8, 14], [0, 1, 11, 12, 12], [0, 6, 2, 3, 9]]
# [0, 0, 0 , 0 , 0 ] Rangée inutile, mais pratique pour l'indexation
# [0, 3, 10, 8 , 14]
# [0, 1, 11, 12, 12]
# [0, 6, 2 , 3 , 9 ]
# grille[1,4] == 14 # par exemple

# Vous devrez arrangé le code qui suit lorsque votre code sera fonctionnel pour l'exemple:
# for i in range(1,M+1):
#     ligne_i = input().split()    # ligne_i = ["0", "3", "10", "8", "14"]
#     for j in range(1,N+1):
#         grille[i][j] = # à compléter


def facteurs(n):
    """Vous devez créer une fonction qui retourne une liste des paires de facteurs de n.

    Args:
        n (int): entier à décomposer en x*y

    Returns:
        liste de tuples (x,y): Une liste de toutes les factorisations (x,y) telles que x*y=n
    """
    l = []
    # exemple: si n=6
    # return [(1,6), (2,3), (3,2), (6,1)]
    return l

# cet ensemble contiendra tous les entiers visités dans la grille
entiers_visites = set()
entiers_visites.add(1) #visiter la case (1,1) est comme avoir encontré l'entier 1 dans la grille

# cette queue (implémenter avec une liste) contient tous coordonnées qui reste a visité.
coord_a_visiter = []
x = 1
y = 1
coord_a_visiter.append((x,y))

# tant qu'il reste des coordonnées à visiter, explorer la grille
while len(coord_a_visiter) >= 1:
    x,y = coord_a_visiter.pop()
    n = grille[x][y]

    # si l'entier n n'est pas dans les entiers visités
        # 1. A-t-on trouvé un entier qui permet de se rendre à la sortie?
        # 2. Rajoutons n aux entiers visités
        # 3. Rajoutons tous les factorisations de n à coord_a_visiter
            # utiliser la fonction extend pour rajouter une liste à la liste
    
    # sinon tous les coordonnées à visiter sont déjà dans la liste à visiter; il n'y a rien à faire.

# Si notre code ce rend à cette ligne ci, nous n'avons pas trouvé la sortie en ayant visité tous les cases possibles...