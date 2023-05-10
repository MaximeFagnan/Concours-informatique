"""
@author: Maxime Fagnan
@email: maxime.fagnan@brebeuf.qc.ca

-Commentaires possiblement a nettoyer
"""

#------------ def Fonctions ------------

#Trouve le meilleur candidat sous (row,col) (inclusif)
def findBelow(row,col,trees):
    limD=n
    limG=-1
    sol_max=n-row
    #Trier les arbres par rangée, puis par colonne
    s_trees=sorted(trees,key=lambda t:(t[0],t[1]))
    #réduire la solution possible à chaque fois que l'on rencontre un arbre
    for t in s_trees:
        r=t[0]
        c=t[1]
        if(r>=row): #ne pas prendre en compte les arbres plus hauts que row
            d_Ver=r-row+1 #distance verticale de row à l'arbre (inclusif)
            #Ajout de l'arbre aux contraintes gauche et droite
            if(c>=col): limD=min(limD,c)
            if(c<=col): limG=max(limG,c)
            d_Hor= limD-limG-1 #distance max entre les arbres pris en compte
            #ajustement de la solution maximale:
            if(d_Ver>sol_max):
                # t trop bas pour influencer les contraintes déjà trouvées.
                return sol_max 
            if(d_Ver>d_Hor):
                # t réduit trop la dist horizontale. La solution est au dessus.
                return d_Ver-1 
            else :
                # t réduit possiblement la solution maximale, mais continuons d'explorer.
                sol_max=min(d_Hor,sol_max) 
    return sol_max

#------------ debut ------------

#traitement des donnÃ©es
n=int(input()) #Matrice de taille n
t=int(input()) #Nombre d'arbres
trees=[] #Liste contenant tous les arbres
treesT=[] #Liste contenant tous les arbres pour une matrice M transposée
while(t>0):
    s=input().split()
    coord=list(map(int,s))
    coord[0]-=1
    coord[1]-=1
    trees.append(coord)
    treesT.append((coord[1],coord[0]))
    t=t-1
treesT=[list(reversed(coord)) for coord in trees]  

#sorted(trees,key=lambda t:(t[0],t[1]))

#Solution initiale (commencer a partir d'en haut)
sol=max(findBelow(0, 0, trees),0)


#Trouver les solutions en dessous de chaque arbre
for t in trees:
    row=t[0]
    col=t[1]
    temp=[sol]
    if(row!=n-1):
        temp.append(findBelow(row+1,col,trees))
    if (col!=n-1):
        #Transposer la matrice permet de réutiliser la fonction findBelow
        temp.append(findBelow(col+1,row,treesT))
    sol=max(temp)
  
print(sol)