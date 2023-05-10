# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:38:27 2022

@author: Maxime Fagnan
@email: fagnan.maxime@courrier.uqam.ca
@email: maxime.fagnan@brebeuf.qc.ca

Ce code ne va que chercher des points pour m==n
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

#algorithme glouton qui essaie tjrs de descendre le compte le plus possible
decompte=k-n
piece=[1]
lastRepIndex=0
#loop de 2 a n
for i in range(2,n+1):
    mx=i-lastRepIndex-1
    #Prendre la solution la plus gloutonne
    if(decompte>=mx):
        piece.append(i)
        decompte-=(mx)
    # elif():
    #     #incomplete
    else: #prendre la note qui nous avance le plus
        lastRepIndex=i-decompte-1
        note=piece[lastRepIndex-1]
        piece.append(note)
        decompte=0

#impression de la piece composer
string=""
for note in piece:
    string+=str(note)+" "
print(string.strip())