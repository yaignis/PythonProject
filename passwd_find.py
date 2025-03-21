import random
import time
mot_de_passe = input("Choisir le mot de passe: ")  # le mot de passe à trouver


def mot_aleatoire(longueur):
    lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    mot_genere = ""
    for carac in range(0, longueur):
        mot_genere = mot_genere + lettres[random.randint(0, len(lettres) - 1)]
    return mot_genere


debut = time.time()
while True:
    mot_alea = mot_aleatoire(len(mot_de_passe))
    print("Mot de passe teste: " + mot_alea)
    if mot_de_passe == mot_alea:
        print("Mot de passe trouve: " + mot_alea)
        fin = time.time() - debut
        print("Trouve en " + str(fin) + " second")
        break
print("Hello Hrun")