import csv

print("1-a- Début de l'opération de nettoyage du fichier original. Ouvrez stadium_sorties.csv pour lire le fichier résultat.")
with open('stadiums_20150302.csv') as fin:
    with open('stadiums_sortie.csv', 'w', newline='\n') as fout:
        ecriteur = csv.writer(fout, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        total = 0
        for ligne in fin:
            token = ligne.split(',')
            ecriteur.writerow( (token[0].strip(), token[2].strip(), token[3].strip(), token[4].strip().strip('"'), token[7].strip()) )
            total+=1

print(f"1-b- Nous avons au total {total} y compris la ligne d'entête, donc {total - 1} lignes de données")