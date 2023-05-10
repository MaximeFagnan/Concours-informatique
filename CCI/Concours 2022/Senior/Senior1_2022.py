# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:07:55 2022

@author: Maxime Fagnan
@email: maxime.fagnan@brebeuf.qc.ca

"""
# --- Algorithme naif ---
n=int(input())
d=int(n/5) #nombre de fois que l'on peut retrouver 5 dans n
count=0
for i in range(d+1):
    remainder=n-i*5
    if(remainder%4==0): count+=1

print(count)