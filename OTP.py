import random

def generate_key(length):
    return ''.join([chr(random.randint(0, 255)) for _ in range(length)])

def otp_encrypt(message, key):
    encrypted = ''.join([chr(ord(m) ^ ord(k)) for m, k in zip(message, key)])
    return encrypted

def otp_decrypt(encrypted, key):
    decrypted = ''.join([chr(ord(e) ^ ord(k)) for e, k in zip(encrypted, key)])
    return decrypted

# Exemplo
message = "HELLO"
key = generate_key(len(message))
encrypted_message = otp_encrypt(message, key)
decrypted_message = otp_decrypt(encrypted_message, key)

print(f"Message: {message}")
print(f"Key: {key}")
print(f"Encrypted: {encrypted_message}")
print(f"Decrypted: {decrypted_message}")
