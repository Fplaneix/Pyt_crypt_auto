#Commentaires

import datetime
dateJour = datetime.datetime.today().strftime('%Y-%m-%d')
dateJourHeure = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')


chemin_log = "../Python/LOG"
chemin_archives = "../Python/ARCHIVES"
chemin_archive_log = "../Python/LOG/ARCHIVES"
chemin_in = "../Python/IN"
chemin_toMail = "../Python/toMail"
clefAES256 = '123456789='
nom_fichier ='texte.txt'

#Print
print ('Fichier main dateJour =>'+dateJour)
print ('Fichier main dateJourHeure =>'+dateJourHeure)
