M = int(input())
N = int(input())
sortie = M*N

# Notons que grille[0][j] et grille[i][0] seront 0 pour notre convénience
grille = [[0]*(N+1) for i in range(M+1)]
# pour accéder à l'élément en position (i,j) grille[i][j]

for i in range(1,M+1):
    ligne_i = input().split()    # ligne_i = ["3", "10", "8", "14"]
    for j in range(1,N+1):
        grille[i][j] = int(ligne_i[j-1])

def facteurs(n):
    """Vous devez créer une fonction qui retourne une liste des paires de facteurs de n.

    Args:
        n (int): entier à décomposer en x*y

    Returns:
        liste de tuples (x,y): Une liste de toutes les factorisations (x,y) telles que x*y=n
    """
    l = []
    for i in range(1,int((n)**(1/2)+1)):
        if n % i == 0:
            x,y = i, n//i
            if x<=M and y<=N :
                l.append((x,y))
            if x<=N and y<=M :
                l.append((y,x))
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
    x,y = coord_a_visiter.pop(0)
    n = grille[x][y]

    # Peut-on se rendre à la sortie?
    if (n == sortie):
        print("yes")
        exit()

    # si l'entier n = grille[x][y] n'est pas dans les entiers visités
    if not (n in entiers_visites):
        # 2. Rajoutons n aux entiers visités
        entiers_visites.add(n)
        # 3. Rajoutons tous les factorisations de n à coord_a_visiter
        coord_a_visiter.extend(facteurs(n)) # utiliser la fonction extend pour rajouter une liste à la liste        
    
    # sinon tous les coordonnées à visiter sont déjà dans la liste à visiter; il n'y a rien à faire.

# Si notre code ce rend à cette ligne ci, nous n'avons pas trouvé la sortie en ayant visité tous les cases possibles...
print("no")