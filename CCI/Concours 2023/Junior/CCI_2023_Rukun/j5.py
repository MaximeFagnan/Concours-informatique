word=input()
r=int(input())
c=int(input())

#objet pour rechercher les mots dans la grille
class GridSearcher:
    def __init__(self,r,c,grid):
        self.size=(r,c)
        self.grid=grid

    #fonction qui trouve les endroits pour partir la recherche
    def search(self,target):
        match=0
        for r in range(self.size[0]):
            for c in range(self.size[1]):
                if self.grid[r][c]==target[0]:
                    match+=self.searchStep(r,c,0,0,1,target) #appeler la fonction qui retourne 1 (mot valide) ou 0 (mot invalide)
        return match #réponse du problème

    #fonction récursive qui vérifie si la suite dans la grille correspond au mot
    def searchStep(self,r,c,dir,switched,no,target):
        """
        dir=direction emprunté pour arriver à cette case (représenté par un nombre entre 1 et 8. 0=situation initiale, donc aucune direction)
        switched=nombre de virage
        no=position de la lettre dans le mot
        target=mot recherché
        """

        if switched==3:return 0 #arrêter la recherche si la suite comporte 2 virages (la variable commence à 1)
        if no==len(target):return 1 # ne pas chercher plus loin que la longueur du mot+1
        letter=target[no]
        found=0

        #appeler la prochaine itération si la lettre de la prochaine case en bonne
        if dir in (0,1,3,5,7): #directions horizontales ou verticales
            if r-1>=0 and self.grid[r-1][c]==letter:found+=self.searchStep(r-1,c,1,switched+int(dir!=1),no+1,target)
            if c+1<self.size[1] and self.grid[r][c+1]==letter:found+=self.searchStep(r,c+1,3,switched+int(dir!=3),no+1,target)
            if r+1<self.size[0] and self.grid[r+1][c]==letter:found+=self.searchStep(r+1,c,5,switched+int(dir!=5),no+1,target)
            if c-1>=0 and self.grid[r][c-1]==letter:found+=self.searchStep(r,c-1,7,switched+int(dir!=7),no+1,target)

        if dir in (0,2,4,6,8): #directions diagonales
            if r-1>=0 and c-1>=0 and self.grid[r-1][c-1]==letter:found+=self.searchStep(r-1,c-1,8,switched+int(dir!=8),no+1,target)
            if r-1>=0 and c+1<self.size[1] and self.grid[r-1][c+1]==letter:found+=self.searchStep(r-1,c+1,2,switched+int(dir!=2),no+1,target)
            if r+1<self.size[0] and c+1<self.size[1] and self.grid[r+1][c+1]==letter:found+=self.searchStep(r+1,c+1,4,switched+int(dir!=4),no+1,target)
            if r+1<self.size[0] and c-1>=0 and self.grid[r+1][c-1]==letter:found+=self.searchStep(r+1,c-1,6,switched+int(dir!=6),no+1,target)

        #retourner le nombre de mots valides qui partent de cette branche. Peut être 0, 1, 2, 3,. ..
        return found

#définir la grille
grid=[]
for i in range(r):
    grid.append(input().split(" "))

g=GridSearcher(r,c,grid)
ans=g.search(word)
print(ans)
