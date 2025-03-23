import string
import random
import time

mot_de_passe = input("Choisir le mot de passe: ")  # mod de passe a trouve


def mot_aleatoire():
    lettres = string.digits + string.ascii_letters + string.punctuation
    suiv = ""
    resultat = ""
    for i in range(len(mot_de_passe)):
        while mot_de_passe[i] != suiv:
            print(resultat + suiv)
#            time.sleep(0.05)
            suiv = random.choice(lettres)
        resultat += suiv
    return resultat


debut = time.time()
print(mot_aleatoire())
fin = time.time() - debut
print("Trouve en " + str(fin) + " second")
