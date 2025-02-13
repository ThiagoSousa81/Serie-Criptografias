from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

# Função para gerar uma chave DES com verificação de paridade
def generate_des_key():
    key = get_random_bytes(8)  # Gera uma chave de 8 bytes
    # Ajusta a chave para incluir bits de paridade
    key_with_parity = bytearray()
    for byte in key:
        # Calcula o bit de paridade
        parity_bit = 1 if bin(byte).count('1') % 2 == 0 else 0
        # Adiciona o byte com o bit de paridade
        key_with_parity.append((byte & 0xFE) | parity_bit)  # Zera o último bit e adiciona o bit de paridade
    return bytes(key_with_parity)

# Função para gerar um IV
def generate_iv():
    return get_random_bytes(8)  # Gera um IV de 8 bytes

# Função para criptografar a mensagem usando DES
def des_encrypt(message, key, iv):
    des = DES.new(key, DES.MODE_CBC, iv)  # Cria um objeto DES com modo CBC
    # Preenche a mensagem para que seu tamanho seja múltiplo de 8
    padding_length = 8 - len(message) % 8
    padded_message = message + (chr(padding_length) * padding_length)
    encrypted_bytes = des.encrypt(padded_message.encode('utf-8'))
    return base64.b64encode(iv + encrypted_bytes).decode('utf-8')  # Retorna IV + mensagem criptografada em Base64

# Função para descriptografar a mensagem usando DES
def des_decrypt(encrypted_message, key):
    encrypted_bytes = base64.b64decode(encrypted_message)
    iv = encrypted_bytes[:8]  # Extrai o IV
    encrypted_bytes = encrypted_bytes[8:]  # O restante é a mensagem criptografada

    des = DES.new(key, DES.MODE_CBC, iv)  # Cria um objeto DES com modo CBC
    decrypted_bytes = des.decrypt(encrypted_bytes)
    # Remove o preenchimento
    padding_length = decrypted_bytes[-1]
    return decrypted_bytes[:-padding_length].decode('utf-8')

# Exemplo de uso
message = "HELLO"
key = generate_des_key()
iv = generate_iv()

# Definindo uma chave e um IV fixos para testes
key = bytes.fromhex('7E1C096E330A5D06')  # Chave fixa
iv = bytes.fromhex('EF6F408059B616CE')    # IV fixo

encrypted_message = des_encrypt(message, key, iv)
decrypted_message = des_decrypt(encrypted_message, key)

print(f"Message: {message}")
print(f"Key (HEX): {key.hex()}")  # Exibe a chave em formato legível
print(f"IV (HEX): {iv.hex()}")    # Exibe o vetor em formato legível
print(f"Encrypted: {encrypted_message}")
print(f"Decrypted: {decrypted_message}")