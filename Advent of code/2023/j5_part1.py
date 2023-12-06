import re
import math
import sys

nom_de_fichier = "Advent of code\\2023\\j5.in" 

# info format: (the destination range start, the source range start, and the range length)
# info format: (d,s,r)

########################################################################

# Structure de donnée


class Conversion_value:
    d=0
    s=0
    r=0

    def __init__(self,conv_strings) -> None:
        parsed_string = list(map(int,conv_strings))
        self.d = parsed_string[0]
        self.s = parsed_string[1]
        self.r = parsed_string[2]

    def __str__(self) -> str:
        return (self.d,self.s,self.r)

class Conversion_map:
    nom = ""
    
    __conversion_rules = dict()
    
    def __init__(self) -> None:
        self.__conversion_rules = dict()
        pass

    def name(self, bla_to_blabla):
        self.nom = bla_to_blabla
    
    def add_conversion(self,conv_strings):
        c_value = Conversion_value(conv_strings)
        self.__conversion_rules[range(c_value.s,c_value.s + c_value.r)] = range(c_value.d, c_value.d + c_value.r)
    
    def find_conversion_rule(self, x: int) :
        """for a given value of x, find conversion rule in __conversions dict
        """
        for r_s,r_d in self.__conversion_rules.items():
            if x in r_s: 
                return (r_s,r_d)
        return None

    def convert(self, x: int) -> int:
        """Convert a value following the map

        Args:
            x (int): value to convert

        Returns:
            int: conversion following the conversion map
        """
        rule = self.find_conversion_rule(x)
        if rule:
            r_s = rule[0]
            r_d = rule[1]
            y = r_d.start + (x-r_s.start)
            return y
        return x
    
    def __str__(self) -> str:
        return str(list(map(Conversion_value.__str__,self.__conv_rules)))

########################################################################

# Partie 1

soln = 0
seeds = []
conversion_maps = []


with open(nom_de_fichier, "r") as f:
    content = f.readlines()
    seeds = list(map(int, content[0].split()[1:])) # [1:] removes "seeds:"

    conv_map = Conversion_map()
    for line in content[3:]: # skip "seed-to-soil map" line
        l = line.split()
        
        # blabla-to-bla map
        if len(l) == 2:
            if conv_map : # None check for initialization
                conv_map.name(l[0] + " " + l[1])
                conversion_maps.append(conv_map)
            conv_map = Conversion_map()

        # destination source range
        elif len(l) == 3:
            conv_map.add_conversion(l)
conversion_maps.append(conv_map)

def conv_seed_to_location(seed_no):
    x = seed_no
    c_map : Conversion_map
    for c_map in conversion_maps:
        x = c_map.convert(x)
    return x

soln = min(list(map(conv_seed_to_location,seeds)))
print(soln)