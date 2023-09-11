"""---------plan---------
1. Compter le nombre d'échanges pour placer correctement tous les livres L à gauche, c'est-à-dire le nombre d'intrus dans les positions 0 à n_l
2. Similairement, compter le nombre d'échanges pour placer correctement tous les livres M au centre, c'est-à-dire le nombre d'intrus dans les positions n_l à n_l+n_m
3. Soustraire le nombre d'échanges commun, c'est-à-dire une échange qui place à la fois un livre L et M
    Ceci correspond à la plus petite valeur entre [#livres M de 0 + n_l] et [#livres L de n_L + n_l+n_m]
!!! En plaçant les livres L et M, tous les livres S sont automatiquement placés"""

livres = input()

n_l = livres.count("L")
n_m = livres.count("M")

échanges = (n_l - livres[:n_l].count("L")) + (n_m - livres[n_l:n_l+n_m].count("M"))
échanges -= min(livres[:n_l].count("M"), livres[n_l:n_l+n_m].count("L"))

print(échanges)