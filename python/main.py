import os
import random
import string
import SDES as SDES
import RSA as RSA
import AES as AES
import trace_reseaux as tr
from experiences import temps_execution_chiffrement, temps_execution_dechiffrement

dir_path = os.path.dirname(os.path.realpath(__file__))

message = "Test de chiffrement avec le double SDES"

# Chiffrement d'un message avec le double SDES
message_chiffre = SDES.double_encrypt_text(message, 143, 977)
print("Message chiffré avec le double SDES : ", message_chiffre)

# Déchiffrement d'un message avec le double SDES
message_dechiffre = SDES.double_decrypt_text(message_chiffre, 143, 977)
print("Message déchiffré avec le double SDES : ", message_dechiffre)

# Cassage brtual
print(SDES.cassage_brutal(message, message_chiffre))

# Cassage astucieux
print(SDES.cassage_astucieux(message, message_chiffre))

# Création des clés provate.pem et public.pem dans data
RSA.generer_couple_cles()

message = b'Test de chiffrement avec le RSA'

# Récupération des clés
private_key = open(os.path.join(dir_path, '../data', 'private.pem')).read()
public_key = open(os.path.join(dir_path, '../data', 'public.pem')).read()

# Chiffrement d'un message avec le RSA
ciphertext = RSA.encrypt(message, public_key)
print("Le message chiffré avec le RSA :", ciphertext)

# Déchiffrement d'un message avec le RSA
decrypted = RSA.decrypt(ciphertext, private_key)
print("Le message déchiffré avec le RSA :", decrypted)

message = b'Test de chiffrement AES avec CBC et un padding PKCS7'

# Création d'une clé aléatoire de 128 bits
key = ''.join([str(random.randint(0, 1)) for _ in range(128)])
key = int(key, 2).to_bytes(len(key) // 8, byteorder='big') # Conversion en bytes

# Chiffrement d'un message avec AES
ciphertext = AES.encrypt(key, message)
print("Le message chiffré avec AES :", ciphertext)

decrypted = AES.decrypt(key, ciphertext)
print("Le message déchiffré avec AES :", decrypted)

# Récupération de la clé dans l'image rossignol2.bmp
key = AES.dechiffrer_image(os.path.join(dir_path, '../data', 'rossignol2.bmp'))
print(f'La clé contenu dans l\'image rossignol2.bmp est : {key} (en hexadécimal : {hex(int(key, 2))})')

# Filtrage des paquets UDP envoyés et reçus sur le port 9999
paquets = tr.get_messages_UDP_9999(open(os.path.join(dir_path, '../data', 'trace_sae.cap'), 'rb'))
print("Les paquets UDP envoyés et reçus sur le port 9999 :", paquets)

# La clé contenue dans l'image rossignol2.bmp multipliée par 4
key = "1110011101101101001100010011111110010010101110011001000001001100111001110110110100110001001111111001001010111001100100000100110011100111011011010011000100111111100100101011100110010000010011001110011101101101001100010011111110010010101110011001000001001100"
key = int(key, 2).to_bytes(len(key) // 8, byteorder='big') # Conversion en bytes
# Déchiffrement des paquets UDP envoyés et reçus sur le port 9999 avec affichage des sources et messages
print("Les paquets UDP envoyés et reçus sur le port 9999 déchiffrés avec la clé contenue dans l'image rossignol2.bmp multipliée par 4 :", tr.decrypt_traffic(os.path.join(dir_path, '../data', 'trace_sae.cap'), key))

# Définition des textes à utiliser pour les graphiques allant de 2 à 20 caractères
lettres_persanes = open(os.path.join(dir_path, '../data', 'lettres_persanes.txt'), 'r').read()
arsene_lupin_extrait = open(os.path.join(dir_path, '../data', 'arsene_lupin_extrait.txt'), 'r').read()
liste_texte_1 = [lettres_persanes[:2], arsene_lupin_extrait[:4], lettres_persanes[:6],
                 arsene_lupin_extrait[:8], lettres_persanes[:10], arsene_lupin_extrait[:12],
                 lettres_persanes[:14], arsene_lupin_extrait[:16], lettres_persanes[:18],
                 arsene_lupin_extrait[:20]]
liste_texte_2 = [arsene_lupin_extrait[:2], lettres_persanes[:4], arsene_lupin_extrait[:6],
                  lettres_persanes[:8], arsene_lupin_extrait[:10], lettres_persanes[:12],
                  arsene_lupin_extrait[:14], lettres_persanes[:16], arsene_lupin_extrait[:18],
                  lettres_persanes[:20]]

# Affichage des graphiques
# Le premier graphique représente le temps d'exécution en fonction de la taille du texte et d'une clé de taille aléatoire entre 0 et 10
# Le deuxième graphique représente le temps d'exécution en fonction de la taille du texte et d'une clé de taille aléatoire entre 0 et 20
SDES.graphique_temps_execution_cassages(liste_texte_1, 10)
SDES.graphique_temps_execution_cassages(liste_texte_2, 20)

# Définition d'un message au hasard de 214 caractères
message = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(214))

# Affichage des graphiques
# Le premier graphique représente le temps d'exécution du chiffrement des deux méthodes sur 200 itérations
# Le deuxième graphique représente le temps d'exécution du déchiffrement des deux méthodes sur 200 itérations
temps_execution_chiffrement(message, 200)
temps_execution_dechiffrement(message, 200)
