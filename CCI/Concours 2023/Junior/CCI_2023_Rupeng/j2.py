#définir un dictionnaire des SHU en fonction de différents piments
SHU = {
    "Poblano":1500,
    "Mirasol":6000,
    "Serrano":15500,
    "Cayenne":40000,
    "Thai":75000,
    "Habanero":125000
}

piquant = 0
N = int(input())

#ajouter au piquant total la valeur SHU de chacun des N piments dans la liste
for _ in range(N):
    piment = input()
    piquant += SHU[piment]
    
print(piquant)