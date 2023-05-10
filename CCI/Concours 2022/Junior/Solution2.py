# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 01:08:50 2022

@author: Maxime Fagnan
@email: fagnan.maxime@courrier.uqam.ca
@email: maxime.fagnan@brebeuf.qc.ca

"""

n=int(input())
nb_golden=0
for i in range(n):
    points=int(input())
    fouls=int(input())
    stars=points*5-fouls*3
    if(stars>40):
        nb_golden+=1

if(nb_golden==n):
    print(str(nb_golden)+"+")
else:
    print(nb_golden)    