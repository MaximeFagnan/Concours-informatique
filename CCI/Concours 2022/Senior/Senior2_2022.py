# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 13:57:04 2022

@author: Maxime Fagnan
@email: maxime.fagnan@brebeuf.qc.ca

"""

#--- def ---


#--- debut ---

#dictionnaire de contrainte de rassemblement pour recherche rapide
x=int(input())
ensemble=dict()
for i in range(x):
    s=input().split()
    if(s[0] not in ensemble):
        ensemble[s[0]]=[]
    ensemble[s[0]].append(s[1])

#dictionnaire de contrainte de separation pour recherche rapide
y=int(input())
separer=dict()
for i in range(y):
    s=input().split()
    if(s[0] not in separer):
        separer[s[0]]=[]
    separer[s[0]].append(s[1])

g=int(input())
groupe=[]
for i in range(g):
    s=input().split()
    groupe.append(s)

c=0 #nb de contraintes observer
for gr in groupe:
    #pour chaque nom de chaque groupe
    for name1 in gr:
        #voir si ce nom est associer a une contrainte de separation
        if(name1 in separer):
            #verifier chaque contrainte de separation
            for name2 in separer[name1]:
                if(name2 in gr): c+=1
        #voir si ce nom est associer a une contrainte de regroupement
        if(name1 in ensemble):
            #verifier chaque contrainte de rassemblement
            for name2 in ensemble[name1]:
                if(name2 not in gr): c+=1

print(c)