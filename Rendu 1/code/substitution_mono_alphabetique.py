"""Module permettant de déchiffrer un message selon la méthode de substitution mono-alphabétique"""

import sys
from unidecode import unidecode

def decode_monoalphabetic_substitution(message: str, key: str) -> str:
    """Permet de déchiffrer un message selon la méthode de substitution mono-alphabétique

    Args:
        message (str): le message à déchiffrer
        key (str): la clé de déchiffrement

    Returns:
        str: le message déchiffré
    """
    res: str = ''
    for lettre in message:
        if lettre.isalpha():
            if lettre.isupper():
                res += key[ord(unidecode(lettre)) - ord('A')]
            else:
                res += key[ord(unidecode(lettre)) - ord('a')]
        else:
            res += lettre
    return res

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage:', 'python3', sys.argv[0], '"<message>" "<cle>"')
        sys.exit(1)
    else:
        print(decode_monoalphabetic_substitution(sys.argv[1], sys.argv[2]))
