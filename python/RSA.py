from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def generer_couple_cles():
    """Permet de générer un couple de clés RSA et de les stocker dans les fichiers data/private.pem et data/public.pem

    Returns:
        tuple: Le couple de clés généré
    """
    key = RSA.generate(2048)
    with open(os.path.join(dir_path, '../data', 'private.pem'), 'wb') as f:
        f.write(key.exportKey('PEM'))
    with open(os.path.join(dir_path, '../data', 'public.pem'), 'wb') as f:
        f.write(key.publickey().exportKey('PEM'))

def encrypt(message, public_key):
    """Permet de chiffrer un message avec une clé publique RSA

    Args:
        message (bytes): Le message à chiffrer
        public_key (str): La clé publique RSA

    Returns:
        bytes: Le message chiffré
    """
    key = RSA.importKey(public_key)
    return PKCS1_OAEP.new(key).encrypt(message)

def decrypt(ciphertext, private_key):
    """Permet de déchiffrer un message avec une clé privée RSA

    Args:
        ciphertext (bytes): Le message chiffré
        private_key (str): La clé privée RSA

    Returns:
        str: Le message déchiffré
    """
    key = RSA.importKey(private_key)
    return PKCS1_OAEP.new(key).decrypt(ciphertext).decode('utf-8')