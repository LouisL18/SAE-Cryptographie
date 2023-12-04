"""Module permettant de déchiffrer un message selon la méthode de césar"""

import sys
from unidecode import unidecode

def decode_cesar(message: str, shift: int) -> str:
    """Permet de déchiffrer un message selon la méthode de césar

    Args:
        message (str): le message à déchiffrer
        shift (int): le décalage à appliquer

    Returns:
        str: le message déchiffré
    """
    res: str = ''
    for lettre in message:
        if lettre.isalpha():
            if lettre.isupper():
                res += chr((ord(unidecode(lettre)) - shift - ord('A')) % 26 + ord('A'))
            else:
                res += chr((ord(unidecode(lettre)) - shift - ord('a')) % 26 + ord('a'))
        else:
            res += lettre
    return res

def dumb_brute_force(message: str) -> str:
    """Permet de déchiffrer un message selon la méthode de césar en
       testant tous les décalages possibles

    Args:
        message (str): le message à déchiffrer

    Returns:
        str: tous les messages déchiffrés avec leur décalage respectif
    """
    res: str = ''
    for shift in range(26):
        res += str(shift) + ' ➜ ' + decode_cesar(message, shift) + '\n'
    return res

def smart_brute_force(message: str) -> str:
    """Permet de déchiffrer un message selon la méthode de césar en
       utilisant un dictionnaire de mots français

    Args:
        message (str): le message à déchiffrer

    Returns:
        str: le message déchiffré
    """
    max_accuracy: int = 0
    best_res: str = ''
    words_list: set[str] = text_to_set('fr.txt')
    for shift in range(26):
        decoded_message: str = decode_cesar(message, shift)
        accuracy: int = sum(1 for word in decoded_message.split(' ') if word.lower() in words_list)
        if accuracy > max_accuracy:
            max_accuracy: int = accuracy
            best_res: str = decoded_message
    return best_res

def text_to_set(file: str) -> set[str]:
    """Permet de mettre tous les mots d'un fichier dans un set

    Args:
        file (str): le nom du fichier

    Returns:
        set: le set contenant tous les mots du fichier
    """
    return set(open(file, 'r', encoding='utf8').read().split('\n'))

if __name__ == "__main__":
    if len(sys.argv) > 2:
        if sys.argv[1] == 'decode':
            if len(sys.argv) != 4:
                print('Usage:', 'python3', sys.argv[0], 'decode "<message>" <decalage>')
                sys.exit(1)
            else:
                print(decode_cesar(sys.argv[2], int(sys.argv[3])))
        elif sys.argv[1] == 'dumb':
            print(dumb_brute_force(sys.argv[2]))
        elif sys.argv[1] == 'smart':
            print(smart_brute_force(sys.argv[2]))
        else:
            print('Usage:', 'python3', sys.argv[0], '<decode|dumb|smart> "<message>" [<decalage>]')
            sys.exit(1)
    else:
        print('Usage:', 'python3', sys.argv[0], '<decode|dumb|smart> "<message>" [<decalage>]')
        sys.exit(1)
