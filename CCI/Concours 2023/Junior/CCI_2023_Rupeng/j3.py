#---------plan---------
#Créer une liste qui contient le nombre de personnes pouvant participer pour chacunes des journées
#Itérer à travers les disponibilités de chaque participant en mettant à jour la liste ci-haut
#Déterminer la valeur maximale présente dans la liste
#Donner l'indice de toutes les journées dont le nombre de disponibilité correspond à la valeur maximale

jours = [0]*5 #[0, 0, 0, 0, 0]

#Itérer à travers la disponibilités de tous les participants
n = int(input())
for _ in range(n):
    disponibilité = list(input()) #(ex: [Y, Y, ., Y, .])

    #i correspond au jour et d correspond à la disponibilité à ce jour
    #enumerate(disponibilité) donne une liste de la forme [(0, Y), (1, Y), (2, .), (3, Y), (4, .)]
    for i, d in enumerate(disponibilité):
        if d == "Y":
            jours[i] += 1 #mettre la liste à jour en incrémentant le nombre de disponibilité à la journée correspondante

disp_max = max(jours) #le maximum de disponibilité dans la liste
jours_max = [str(d[0]) for d in filter(lambda d: d[1]==disp_max, list(enumerate(jours, start=1)))] #liste de toutes les journées où la disponibilité est maximale 
print(",".join(jours_max)) #séparer les journées par une virgule et donner le résultat