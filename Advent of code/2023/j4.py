import re
nom_de_fichier = "Advent of code\\2023\\j4.in" 

# Partie 1
soln = 0
with open(nom_de_fichier, "r") as f:
    for line in f:
        win_nums, my_nums = line.split("|")
        win_nums = set(map(int, re.findall("[0-9]+", win_nums)[1:])) # remove card number
        my_nums = set(map(int, re.findall("[0-9]+", my_nums)))
        my_wins = my_nums.intersection(win_nums)
        if len(my_wins) != 0:
            soln += 2**(len(my_wins)-1)

print(soln)

#################################################################

# Part 2:
soln = 0

with open(nom_de_fichier, "r") as f:
    num_cards_won = [1]*204
    for i, line in enumerate(f):
        win_nums, my_nums = line.split("|")
        win_nums = set(map(int, re.findall("[0-9]+", win_nums)[1:])) # remove card number
        my_nums = set(map(int, re.findall("[0-9]+", my_nums)))
        my_wins = my_nums.intersection(win_nums)
        for j,win in enumerate(my_wins):
            num_cards_won[i+j+1] += num_cards_won[i]

soln = sum(num_cards_won)
print(soln)
