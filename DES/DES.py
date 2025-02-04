from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

# Função para gerar uma chave DES
def generate_des_key():
    return get_random_bytes(8)  # Gera uma chave de 8 bytes

# Função para criptografar a mensagem usando DES
def des_encrypt(message, key):
    des = DES.new(key, DES.MODE_CBC, iv=key)  # Usando a mesma chave como IV para simplicidade (não recomendado para produção)
    # Preenche a mensagem para que seu tamanho seja múltiplo de 8
    padded_message = message + (8 - len(message) % 8) * chr(8 - len(message) % 8)
    encrypted_bytes = des.encrypt(padded_message.encode('utf-8'))
    return base64.b64encode(encrypted_bytes).decode('utf-8')

# Função para descriptografar a mensagem usando DES
def des_decrypt(encrypted_message, key):
    des = DES.new(key, DES.MODE_CBC, iv=key)  # Usando a mesma chave como IV para simplicidade (não recomendado para produção)
    encrypted_bytes = base64.b64decode(encrypted_message)
    decrypted_bytes = des.decrypt(encrypted_bytes)
    # Remove o preenchimento
    padding_length = decrypted_bytes[-1]
    return decrypted_bytes[:-padding_length].decode('utf-8')

# Exemplo de uso
message = "HELLO"
key = generate_des_key()
encrypted_message = des_encrypt(message, key)
decrypted_message = des_decrypt(encrypted_message, key)

print(f"Message: {message}")
#print(f"Key: {key.hex()}")  # Exibe a chave em formato legível
print(f"Key: {str(key)}")
print(f"Encrypted: {encrypted_message}")
print(f"Decrypted: {decrypted_message}")
