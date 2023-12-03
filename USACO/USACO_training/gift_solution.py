# Auteur : Émile Gobeil
import re
"""
ID: username
LANG: PYTHON3
TASK: gift1
"""
#On collecte le input
fin = open ('USACO\USACO_training\gift1.in', 'r')
fout = open ('USACO\USACO_training\gift1.out', 'w')
nb_persons = int(fin.readline())

persons = []
balance_persons = {}
final_balance = {}
recipients_gifters = {}

for i in range(nb_persons):
    name = fin.readline()
    persons.append(name)
    balance_persons[name] = 0
    final_balance[name] = 0

for i in range(nb_persons):
    name = fin.readline()
    balance, nb_recipients = fin.readline().split()
    balance_persons[name] = int(balance)

    recipients = []
    for j in range(int(nb_recipients)):
        recipients.append(fin.readline())
    recipients_gifters[name] = recipients




# On distribue l'argent
for name in persons:
    if recipients_gifters[name] != []:
        #on veut savoir le montant que chaque receveur recoit --> balance_persons[name]: l'argent total --> len(recipients_gifters): le nombre de receveurs
        money_for_recipients = ( balance_persons[name] - ( balance_persons[name] % len(recipients_gifters[name]) )) / len(recipients_gifters[name])

        #on veut savoir le montant que le donneur donne (en negatif)
        money_for_giver = (balance_persons[name] % len(recipients_gifters[name])) - balance_persons[name]
        final_balance[name] += money_for_giver


        #on donne l'argent aux receveurs
        for i in recipients_gifters[name]:
            final_balance[i] += money_for_recipients



# on envoie la reponse avec le bon format
for name in persons:
    fout.write(re.sub('[\W_]+', '', name) + " " + str(int(final_balance[name])) + "\n")

