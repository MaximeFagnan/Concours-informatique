#nombre de personne disponible pour chaque jour
days=[0,0,0,0,0]

#ajuster le nombre de personnes pouvant participer
for _ in range(int(input())):
    dispo=input()
    for i,char in enumerate(dispo):
        if char=="Y":days[i]+=1

maxday=max(days) #le nombre maximal de participants

#identifier tous les jours avec le nombre maximal
possible=[]
for i in range(5):
    if days[i]==maxday:possible.append(str(i+1))

print(",".join(possible))
