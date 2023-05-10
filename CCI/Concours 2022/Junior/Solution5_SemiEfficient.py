# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:08:44 2022

@author: Maxime Fagnan
@email: fagnan.maxime@courrier.uqam.ca
@email: maxime.fagnan@brebeuf.qc.ca

Cette solution dépasse le temps alloué pour les tests sur des matrices de
500 000 cases avec plus de 100 arbres.

Pour arranger la solution, les fonctions findBelow et findRight doivent
etre modifiées afin de ne faire qu'une boucle simple a travers les arbres.
"""

#------------ def Fonctions ------------

#Trouve le meilleur candidat à partir de (row,col) en regardant par en bas
def findBelow(row,col):
    limD=n
    limG=-1
    sol=0
    for i in range(row,n):
        for t in trees:
            if(t[0]==i):
                if(t[1]>=col):
                    limD=min(limD,t[1])
                if(t[1]<=col):
                    limG=max(limG,t[1])
        d_Hor= limD-limG-1
        d_Ver= i-row+1
        if(d_Ver>d_Hor): return sol
        sol=sol+1
    return sol

#Trouve le meilleur candidat à partir de (row,col) en regardant par la droite
def findRight(row,col):
    limB=n
    limH=-1
    sol=0
    for i in range(col,n):
        for t in trees:
            if(t[1]==i):
                if(t[0]>=row): limB=min(limB,t[0])
                if(t[0]<=row): limH=max(limH,t[0])
        d_Ver= limB-limH-1
        d_Hor= i-col+1
        if(d_Hor>d_Ver): return sol
        sol=sol+1
    return sol

#------------ debut ------------

#traitement des données
n=int(input()) #Matrice de n à 0
t=int(input()) #Nombre d'arbres
trees=[] #Liste contenant tous les arbres
while(t>0):
    s=input().split()
    coord=list(map(int,s))
    coord[0]-=1
    coord[1]-=1
    trees.append(coord)
    t=t-1

#Trier les arbres par x, puis par y (pas utile pour cette solution)
sorted(trees,key=lambda t:(t[0],t[1]))

#Solution initiale (commencer a?partir d'en haut)
sol=max(findBelow(0, 0),0)

#Trouvons les solutions ? droite et en dessous de chaque arbre
for t in trees:
    row=t[0]
    col=t[1]
    temp=[sol]
    if(row!=n-1):
        temp.append(findBelow(row+1,col))
    if (col!=n-1):
        temp.append(findRight(row,col+1))
    sol=max(temp)
print(sol)