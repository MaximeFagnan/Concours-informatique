B = int(input())

#calculer la pression atmosphérique selon la formule indiquée
print(5*B - 400)

#Déterminer l'altitude à partir du point d'ébullition de l'eau
if B > 100:print(-1)
elif B < 100:print(1)
else:print(0)