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
numbers = dict() #(row,col) where there is a digit -> number
stars = dict() #(row,col) where there is a * -> 1

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

    #skip this star if it doesn't have exactly two adjacent numbers
    up = "".join(char_matrix[row-1][col-1:col+2])
    left = char_matrix[row][col-1]
    right = char_matrix[row][col+1]
    down = "".join(char_matrix[row+1][col-1:col+2])
    neighbourhood = "_".join([up,left,right,down])
    # .82..
    # ..*..  -> 82._._._.82   (for linear search)
    # ..82.
    if len(re.findall("[0-9]+", neighbourhood)) !=2 : continue

    #find the two adjacent numbers
    adjacent_numbers = set()
    # set is necessary since 82 would be picked up 4 times in the following example:
    # .82..
    # ..*..
    # ..82.
    for i in range(row-1,row+2):
        for j in range(col-1, col+2):
            if i==row and j==col: continue # This is the star itself
            number = numbers.get((i,j)) # None if there is no number at those coords.
            if number :
                adjacent_numbers.add(number)

    if len(adjacent_numbers) == 2:
        soln += adjacent_numbers.pop() * adjacent_numbers.pop()
    elif len(adjacent_numbers) == 1: #if the two adjacent numbers were the same number. 
        soln += adjacent_numbers.pop()**2

print(soln)
