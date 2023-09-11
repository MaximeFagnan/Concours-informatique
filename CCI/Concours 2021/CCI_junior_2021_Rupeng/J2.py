n = int(input())

montant_max = 0
for i in range(n):
    nom, montant = input(), int(input())

    #si le montant est supérieur au montant maximale enregistrée, le nom et le nouveau montant sont mis à jour
    if montant > montant_max:
        montant_max = montant
        nom_max = nom

print(nom_max)