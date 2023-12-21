from scapy.all import rdpcap, UDP
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def get_messages_UDP_9999(cap_file_path):
    """Permet de récupérer les messages UDP sur le port 9999 d'un fichier cap

    Args:
        cap_file_path (str): le chemin du fichier cap

    Returns:
        list: la liste des messages UDP sur le port 9999
    """
    packets = rdpcap(cap_file_path)
    messages = []
    for packet in packets:
        if packet.haslayer(UDP) and (packet[UDP].dport == 9999 or packet[UDP].sport == 9999):
            messages.append(packet)
    return messages

def decrypt_AES_message(message, key):
    """Permet de décrypter un message chiffré avec AES en mode CBC avec padding PKCS7

    Args:
        message (scapy.packet): le message à décrypter
        key (bytes): la clé de chiffrement (32 octets)

    Raises:
        ValueError: si le message n'est pas de la bonne taille

    Returns:
        str: le message décrypté
    """
    if len(message.load[16:]) % 16 != 0:
        raise ValueError(f'Le message ({len(message.load[16:])} octets) n\'est pas de la bonne taille, il doit être un multiple de 16 octets')
    cipher = Cipher(algorithms.AES(key), modes.CBC(message.load[:16]), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(message.load[16:]) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    unpadded = unpadder.update(decrypted) + unpadder.finalize()
    return unpadded.decode()

def decrypt_traffic(cap_file_path, key):
    """Permet de décrypter le payload des messages UDP sur le port 9999 d'un fichier cap utilisant le protocole AES en mode CBC avec padding PKCS #7

    Args:
        cap_file_path (str): le chemin du fichier cap

    Returns:
        list: la liste des messages décryptés sous la forme d'un dictionnaire {adresse source: message décrypté}
    """
    messages = get_messages_UDP_9999(cap_file_path)
    decrypted_messages = []
    for message in messages:
        decrypted_messages.append({message.src: decrypt_AES_message(message[UDP].payload, key)})
    return decrypted_messages