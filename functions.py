#Import
import main_param
#Import os pour parcourir les dossiers
import os
#Import shutil pour déplacer les fichiers
import shutil
#Import cryptography
import crypt
from tkinter import *
from tkinter import simpledialog

#Dialogue box
def popup_chiffrement():
    s = simpledialog.askstring("Renseigner le nom du fichier à crypter", "nom fichier")
    k = simpledialog.askstring("Renseigner la clef de déchiffrement", "Clef de chiffrement")
    crypt.encrypt(s,k)
def popup_dechiffrement():
    s = simpledialog.askstring("Renseigner le nom du fichier à décrypter", "nom fichier")
    k = simpledialog.askstring("Renseigner la clef de déchiffrement", "Clef de chiffrement")
    dechiffrement_fichier(s,k)
#Dialogue box
def init_dialogbox():
    root = Tk()
    root.geometry("300x300")
    button_c = Button(root, text="Chiffrement", command=popup_chiffrement)
    button_d = Button(root, text="Déchiffrement", command=popup_dechiffrement)
    button_c.pack()
    button_d.pack()
    root.mainloop()


#Déplacement de fichiers
def deplacer_fichier():
    source = main_param.chemin_in+'/'+main_param.nom_fichier
    destination = main_param.chemin_toMail+'/'+main_param.nom_fichier
    shutil.move(source,destination)
#Liste des fichiers dans un répertoire
def liste_fichier(dossier):
    FichList = [ f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier,f)) ]
    return FichList
    #a =liste_fichier('../Python/IN')
    #print(a)
def chiffrement_fichier(fichier,key):
    crypt.encrypt(fichier,key)

def dechiffrement_fichier(fichier,key):
    crypt.decrypt(fichier,key)

#Result
print(main_param.dateJour)
key ='Srv0oL5KINlPKmr-WTOmtp5YEp7Avts15JeN8zzdOfU='
#k = crypt.write_key()
#print("Renseigner le nom du Fichier à crypter :")
#fe = input()

#fe = 'texte.txt'
#fc = 'crypt_'+fe
init_dialogbox()
