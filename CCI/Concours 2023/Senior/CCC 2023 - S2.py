# Autheur: Maxime Fagnan
# CCC Senior 2023 - S2

#entree des donnees
n=int(input())
montagnes=input().split()
montagnes=list(map(lambda x :int(x), montagnes))

#programmation dynamique
asymetrie=[]
'''
i: largeur de la photo recadrée (différence de la position de départ et la position de fin)
j: position de départ de la photo recadrée
asymetrie[i][j]: asymétrie de la photo de largeur i en à partir de la position j
'''
asymetrie.append([0]*n) #photo de largeurs 0 parfaitement symétrique
asymetrie.append([])
for j in range(n-1): asymetrie[1].append(abs(montagnes[j]-montagnes[j+1]))
for i in range(2,n):
    asymetrie.append([])
    for j in range(n-i):
        asymetrie[i].append( abs(montagnes[j]-montagnes[j+i]) + asymetrie[i-2][j+1] )

soln=[]
for i in range(n): soln.append(min(asymetrie[i]))
soln=str(soln).replace('[','').replace(']','').replace(',','').strip()
print(soln)


#Solution naïve
""" 
#gap est la distance entre 2 données
#pour chaque gap possible
maximum=sum(montagnes)
soln=[] #update après chaque gap avec minimum
for gap in range(0,n):
    minimum=maximum
    #Evaluer l'asymétrie de tous les listes possibles
    for i in range(n-gap):
        #Calculer de l'asymétrie de la montagne i à la montagne i+gap
        snippet=montagnes[i:i+gap+1]
        asymetrie=0
        for j in range((gap+1)//2):
            asymetrie += abs(snippet[j]-snippet[-j-1])
        minimum= min(minimum, asymetrie) 
    soln.append(minimum)
soln=str(soln).replace('[','').replace(']','').replace(',','').strip()
print(soln)
"""