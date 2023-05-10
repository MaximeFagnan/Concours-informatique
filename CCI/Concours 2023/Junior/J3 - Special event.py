n=int(input())
dispos=[0]*5
for i in range(n):
    preferences=input()
    for j, c in enumerate(preferences):
        if(c=="Y"): dispos[j]+=1

soln=[]
mx=max(dispos)
for i, nb in enumerate(dispos):
    if(nb==mx): soln.append(i+1)

soln2=""
for day in soln:
    soln2 += str(day)+","
print(soln2[:-1])