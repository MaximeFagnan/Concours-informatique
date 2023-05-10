# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 00:35:51 2022

@author: Maxime Fagnan
@email: fagnan.maxime@courrier.uqam.ca
@email: maxime.fagnan@brebeuf.qc.ca

"""

#--- definitions ---

#--- debut ---

entree=input()
nb_de_tours=""
cordes=""
operation=""
for c in entree:
    if(c.isalpha()):
        if(nb_de_tours != ""): #Si tu analyse une lettre après un chiffre
            #Imprime l'opération emmagasiner
            print(f"{cordes} {operation} {nb_de_tours}")
            #RESET pour emmagasiner la prochaine operation
            nb_de_tours=""
            cordes=""
            operation=""
        cordes+=c
    if(c=="+"):
        operation="tighten"
    if(c=="-"):
        operation="loosen"
    if(c.isdigit()):
        nb_de_tours=nb_de_tours+c

#imprimer la dernière operation
print(f"{cordes} {operation} {nb_de_tours}")