from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from PIL import Image
from os import urandom
import os

def encrypt(key, message):
    """Chiffre un message avec AES et une clé de 256 bits.

    Args:
        key (bytes): Clé de 256 bits.
        message (bytes): Message à chiffrer.

    Returns:
        bytes: Message chiffré avec un vecteur d'initialisation de 16 octets.
    """
    iv = urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message) + padder.finalize()
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext

def decrypt(key, ciphertext):
    """Déchiffre un message avec AES et une clé de 256 bits.

    Args:
        key (bytes): Clé de 256 bits.
        ciphertext (bytes): Message chiffré.

    Raises:
        ValueError: Le message n'est pas de la bonne taille, il doit être un multiple de 16 octets.

    Returns:
        str: Message déchiffré.
    """
    if len(ciphertext[16:]) % 16 != 0:
        raise ValueError(f'Le message ({len(ciphertext[16:])} octets) n\'est pas de la bonne taille, il doit être un multiple de 16 octets')
    cipher = Cipher(algorithms.AES(key), modes.CBC(ciphertext[:16]), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ciphertext[16:]) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    unpadded = unpadder.update(decrypted) + unpadder.finalize()
    return unpadded.decode()

def dechiffrer_image(path):
    """Permet de récupérer la clé de chiffrement d'une image en récupérant le bits de poids faible de chaque pixel.

    Args:
        path (str): Chemin vers l'image.

    Returns:
        str: La clé de chiffrement.
    """
    image = Image.open(path)
    pixels = image.load()
    (largeur, hauteur) = image.size
    return ''.join([str(pixels[x, y] % 2) for y in range(hauteur) for x in range(largeur)])[:64]