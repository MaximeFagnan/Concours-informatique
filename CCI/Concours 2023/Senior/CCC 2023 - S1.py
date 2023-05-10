# Autheur: Maxime Fagnan
# CCC Senior 2023 - Q1

#entree des donnees
c=int(input())
l1=input().split()
l2=input().split()

def to_int(c):
    return int(c)

l1=list(map(to_int,l1))
l2=list(map(to_int,l2))

#combien de ruban dans la première allée 
bandes=0
for i,val in enumerate(l1):
    if val==1 :
        if i==0 : bandes+=1
        elif l1[i-1]==0 : bandes+=1

        if i==c-1 : bandes+=1
        elif l1[i+1]==0 : bandes+=1

        #triangle vers le bas
        if i%2 == 0 :
            if(l2[i]==0): bandes+=1
        #triangle vers le haut
        if i%2 == 1 : bandes+=1

#combien de ruban dans la deuxième allée 
for i,val in enumerate(l2):
    if val==1 :
        if i==0 : bandes+=1
        elif l2[i-1]==0 : bandes+=1

        if i==c-1 : bandes+=1
        elif l2[i+1]==0 : bandes+=1

        #triangle vers le haut
        if i%2 == 0 :
            if(l1[i]==0): bandes+=1
        #triangle vers le bas
        if i%2 == 1 : bandes+=1

print(bandes)