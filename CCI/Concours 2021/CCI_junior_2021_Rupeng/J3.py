commandes = []

while True:
    entrée = input()
    if entrée == "99999":break
    
    #séparer la direction et le # de pas (aa/aaa) et additionner les deux chiffres de la direction
    nouvelle_direction, pas = entrée[:2], entrée[2:]
    nouvelle_direction = sum(map(int, nouvelle_direction))

    #sauter directement à l'étape suivante si la somme des deux premiers chiffres est 0
    #sinon, utiliser l'opérateur modulo pour déterminer la parité et mettre à jour la direction
    if nouvelle_direction == 0:pass
    elif nouvelle_direction % 2 == 0:direction = "right"
    else:direction = "left"

    #enregistrer la commande secrète
    commandes.append(f"{direction} {pas}")

print("\n".join(commandes))