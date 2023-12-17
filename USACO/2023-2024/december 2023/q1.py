line_1 = input().split()
N = int(line_1[0])
M = int(line_1[1])

cow_heights = input().split()
cow_heights = list(map(int,cow_heights))

cane_heights = input().split()
cane_heights = map(int,cane_heights)

for cane in cane_heights:
    bottom = 0
    top = cane
    
    for i, cow in enumerate(cow_heights):
        growth = 0

        #eating
        if cow>bottom:
            if cow>top:
                growth = top - bottom
            elif bottom<cow<top:
                growth = cow - bottom
            cow_heights[i] += growth
            bottom += growth
            if bottom == top:
                # No more cane == No more cows can eat
                break
        # or not tall enough sorry
    
    #next cane

for cow in cow_heights:
    print(cow)
