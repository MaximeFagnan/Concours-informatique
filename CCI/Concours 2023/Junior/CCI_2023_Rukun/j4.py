cols=int(input())
r1=input().split(" ")
r2=input().split(" ")

shared=0 #nombre de bordures partagées
total=0 #nombre de bordures totales

#ajustements spéciaux pour le dernier triangle
if r1[-1]=="1":total+=1
if r2[-1]=="1":total+=1
if r1[-1]=="1" and r2[-1]=="1" and not (cols-1)%2:shared+=1

for i in range(cols-1):
    #ajuster rangée du haut
    if r1[i]=="1":
        total+=1
        if r1[i+1]=="1":shared+=1

    #ajuster rangée du bas
    if r2[i]=="1":
        total+=1
        if r2[i+1]=="1":shared+=1
        if r1[i]==r2[i] and not i%2:shared+=1 #ajuster bordure au milieu

#appliquer la formule
print(total*3-shared*2)
