# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:38:27 2022

@author: Maxime Fagnan
@email: maxime.fagnan@brebeuf.qc.ca
"""

from sys import exit

s=input().split()

n=int(s[0]) #nombre de notes
m=int(s[1]) #plus haute note
k=int(s[2]) #nombre de bons echantillons

if(k<n):
    print(-1)
    exit()
if (k>n*(n+1)/2):
    print(-1)
    exit()

if (k>n+(m-1)*m/2+(n-m+1)*(m-1)-1):
    print(-1)
    exit()


#algorithme glouton qui essaie tjrs de descendre le compte le plus possible
decompte=k-n
piece=[1]
lastRepIndex=0
#loop de 2 a n
for i in range(2,n+1):
    mx=i-lastRepIndex-1
    #Prendre la solution la plus gloutonne
    if(decompte>=mx):
        if(mx==m):
            piece.append(piece[i-m-1])
            decompte-=(m-1)
            lastRepIndex=i-m
        else:
            piece.append(i)
            decompte-=(mx)
        
    else: #prendre la note qui nous avance le plus
        if(decompte==0):
            break #nous remplirons efficacement pour la suite
        lastRepIndex=i-decompte-1
        note=piece[lastRepIndex-1]
        piece.append(note)
        decompte=0

if(len(piece)!=n):
    l=n-len(piece)
    remplissage=[piece[-1]]*l
    piece=piece+remplissage

#impression de la piece composer
string=" ".join(map(str,piece))
print(string.strip())