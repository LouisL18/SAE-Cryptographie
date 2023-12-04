"""Module permettant de déchiffrer un message chiffré avec le chiffre de Vigenère"""

import sys
from unidecode import unidecode

def cle_longue(message_chiffre: str, cle: str) -> str:
    """Permets de créer une clé de la même longueur que le message chiffré

    Args:
        message_chiffre (str): message chiffré
        cle (str): cle de chiffrement

    Returns:
        str: clé de la même longueur que le message chiffré
    """
    cle_rep: str = ""
    nb_cle: int = 0
    cle = unidecode(cle)
    for char in message_chiffre:
        if char.isalpha():
            cle_rep += cle[nb_cle % len(cle)].upper()
            nb_cle += 1
        else:
            cle_rep += char
    return cle_rep

def decrypt_vigenere(message_code: str, cle: str):
    """Permet de déchiffrer un message chiffré avec le chiffre de Vigenère

    Args:
        message_code (str): message chiffré
        cle (str): cle de chiffrement

    Returns:
        String: Message déchiffré
    """
    res: str = ""
    if len(cle) == 0:
        return message_code
    cle_rep: str = cle_longue(message_code, cle)
    message_code = unidecode(message_code)
    for ind_lettre in range(len(message_code)):
        if message_code[ind_lettre].isalpha():
            decalage = ord(cle_rep[ind_lettre]) - ord('A')
            lettre_decripte=chr((ord(message_code[ind_lettre].upper())
                                 -decalage-ord('A'))%26+ord('A'))
            if message_code[ind_lettre].islower():
                lettre_decripte = lettre_decripte.lower()
            res += lettre_decripte
        else:
            res += message_code[ind_lettre]
    return res

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage:', 'python3', sys.argv[0], '"<message>" "<cle>"')
        sys.exit(1)
    else:
        print(decrypt_vigenere(sys.argv[1], sys.argv[2]))
