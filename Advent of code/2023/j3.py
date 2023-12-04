import re
nom_de_fichier = "Advent of code\\2023\\j3.in" # a été paddé avec deux ligne de .....

# Partie 1
soln = 0
char_matrix=[]
lines = []
with open(nom_de_fichier, "r") as f:
    for line in f:
        lines.append("."+line.strip()+".") # data padding at start and end of line
        chars=[]
        for char in lines[-1]:
            chars.append(char)
        char_matrix.append(chars)

rows = len(char_matrix)
columns = len(char_matrix[0])

for row,line in zip(range(rows)[1:rows-1],lines[1:columns-1]):
    matches = re.finditer("[0-9]+",line)
    for m in matches:
        number= int(m.group())
        start = m.start()
        end = m.end()-1
        is_valid = False

        for i in range(row-1,row+2):
            for j in range(start-1,end+2):
                if i==row and start<=j<=end: continue
                if re.match("\.|[0-9]+",char_matrix[i][j]): continue
                is_valid = True
        
        if is_valid:
            soln+=number

print(soln)

#################################################################

# Part 2:

soln = 0
numbers = dict()
stars = dict()

for row,line in zip(range(rows)[1:rows-1],lines[1:columns-1]):
    matches = re.finditer("[0-9]+",line)
    for m in matches:
        number= int(m.group())
        start = m.start()
        end = m.end()
        for n in range(start,end):
            numbers[(row,n)] = number

    matches = re.finditer("\*",line)
    for m in matches:
        stars[(row,m.start())] = 1

for row,col in stars:
    adjacent_numbers = set()
    for i in range(row-1,row+2):
        for j in range(col-1, col+2):
            if i==row and j==col: continue # This is the star itself
            if numbers.get((i,j)) :
                adjacent_numbers.add(numbers.get((i,j)))

    if len(adjacent_numbers) == 2:
        soln += adjacent_numbers.pop() * adjacent_numbers.pop()

print(soln)
