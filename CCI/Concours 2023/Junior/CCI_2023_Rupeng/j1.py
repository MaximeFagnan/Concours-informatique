#définir les variables du problème
p = int(input())
c = int(input())

score = 50*p - 10*c

#ajotuer un bonus de 500 point s'il y a plus de colis livrés que de collisions avec les obstacles. 
if p > c:
    score += 500

print(score)