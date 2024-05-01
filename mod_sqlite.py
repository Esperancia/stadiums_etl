import csv
import sqlite3
#Creer la connexion
conn = sqlite3.connect('d05_intra.dbf')

#Creation DDL
cde_ddl = '''create table if not exists STADES(
id integer primary key autoincrement,
Team text, 
City text, 
Stadium text, 
Capacity integer, 
Country text
)
'''
#Creer le curseur
curseur = conn.cursor()
#Creer la table
curseur.execute(cde_ddl)

#insertion
cde = 'insert into STADES(Team, City, Stadium, Capacity, Country)values(?,?,?,?,?)'

with open('stadiums_sortie.csv') as f:
    csv_reader = csv.reader(f)
    next(csv_reader, None)
    for row in csv_reader:
        token = row[0].split(';')
        print(token[3])
        #Team : token[0]; City : token[1]; Stadium : token[2]; Capacity : token[3]; Country : token[4]
        curseur.execute(cde, [token[0].strip('"'), token[1].strip('"'), token[2].strip('"'), token[3].strip('"'), token[4].strip('"')])
        conn.commit()

requete = 'select * from STADES'
curseur.execute(requete)
#parcourir
print('=' * 50)
for rec in curseur:
    print(f'ID:{rec[0:5]}')

conn.close()