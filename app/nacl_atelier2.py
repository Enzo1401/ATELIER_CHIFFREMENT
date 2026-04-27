import nacl.secret
import nacl.utils
from nacl.encoding import HexEncoder

def run_atelier2():
    print("--- Atelier 2 : Chiffrement avec PyNaCl (SecretBox) ---")

    # 1. Génération d'une clé sécurisée de 32 octets
    # SecretBox nécessite une clé de 32 octets exactement
    key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
    box = nacl.secret.SecretBox(key)
    
    print(f"✅ Clé générée (hex) : {key.hex()}")

    # 2. Le message à chiffrer
    message = b"Ceci est un message chiffre avec XSalsa20-Poly1305"
    print(f"Original : {message.decode()}")

    # 3. Chiffrement
    # PyNaCl génère automatiquement un 'nonce' (IV) unique pour chaque message
    encrypted = box.encrypt(message)
    
    # On affiche le résultat en Hexadécimal pour qu'il soit lisible
    print(f"🔒 Chiffré (hex) : {encrypted.hex()}")

    # 4. Déchiffrement
    # La SecretBox extrait elle-même le nonce du message chiffré
    decrypted = box.decrypt(encrypted)
    
    print(f"🔓 Déchiffré : {decrypted.decode()}")

if __name__ == "__main__":
    run_atelier2()