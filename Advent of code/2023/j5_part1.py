nom_de_fichier = "Advent of code\\2023\\j5.in" 

# info format: (the destination range start, the source range start, and the range length)
# info format: (d,s,r)

########################################################################

# Structure de donnée

class Conversion_rule:
    """
    source and dest ranges
    """
    source: range
    dest: range

    def __init__(self, conv_string) -> None:
        #Parses an input_string: (d: dest int, s: source int, r: range length int)
        #into source and destination ranges
        parsed_string = list(map(int,conv_string))
        d = parsed_string[0]
        s = parsed_string[1]
        r = parsed_string[2]
        self.source = range(s, s + r)
        self.dest = range(d, d + r)

    def __str__(self) -> str:
        return (self.d,self.s,self.r)

class Conversion_map:
    """
    conversion map from x-to-y
    
    Example:
    name: "seed-to-soil"
    __conversion_rules = {
        range(98,100) : range(50,52)
        range(50,98)  : range(52,100)
    }

    convert(63) -> 65    # with 2nd rule
    convert(7)  -> 7     # because there is no rule for 7
    """
    
    nom = "" # fluff and testing
    __conversion_rules = dict()
    
    def __init__(self) -> None:
        self.__conversion_rules = dict()
        pass

    # fluff and testing
    def name(self, bla_to_blabla):
        self.nom = bla_to_blabla
    
    def add_conversion(self,conv_string):
        rule = Conversion_rule(conv_string)
        self.__conversion_rules[rule.source] = rule.dest
    
    def find_conversion_rule(self, x: int) -> tuple[range,range] :
        """for a given value of x, find conversion rule in __conversions dict
        """
        for r_s,r_d in self.__conversion_rules.items():
            if x in r_s: 
                return (r_s,r_d)
        return (range(x, x+1),range(x,x+1))

    def convert(self, x: int) -> int:
        """Convert a value following the map

        Args:
            x (int): value to convert

        Returns:
            int: conversion following the conversion map
        """
        r_s, r_d = self.find_conversion_rule(x)
        y = r_d.start + (x-r_s.start)
        return y
    
    # fluff and testing
    def __str__(self) -> str:
        return str(list(map(Conversion_rule.__str__,self.__conv_rules)))

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