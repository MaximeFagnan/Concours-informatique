# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:38:27 2022

@author: Maxime Fagnan
@email: maxime.fagnan@brebeuf.qc.ca
"""
from os import walk
import pathlib

#---def---

def countGoodSamples(piece) -> int():
    """
    finds the # of goodsamples in piece
    """
    last_index=dict()
    count=piece.len()
    for i,note in enumerate(piece):
        if(note in last_index):
            count+=i-last_index[note]-1
            last_index[note]=i
        else:
            count+=i
    return count

#tester
myPath=pathlib.Path(__file__).parent.resolve()

f = []
for (dirpath, dirnames, filenames) in walk(myPath):
    f.extend(filenames)
    break

in_file=[]
out_file=[]

for filename in f:
    if(filename.endswith(".in")):
        in_file.append(filename)
    if(filename.endswith(".out")):
        out_file.append(filename)

