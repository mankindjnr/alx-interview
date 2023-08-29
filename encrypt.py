from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import os

# Generate RSA key pair for asymmetric encryption
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()
print("-----------public key--------------------")
print(public_key)
print("---------------------------------------")
# Generate a random AES key for symmetric encryption
aes_key = Fernet.generate_key()

# Phone number to be encrypted
phone_number = "+1234567890"

# Encrypt the AES key using RSA public key
cipher_rsa = public_key.encrypt(
    aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Encrypt the phone number using the AES key
cipher_suite = Fernet(aes_key)
cipher_text = cipher_suite.encrypt(phone_number.encode())
print("---------------cypher---------------")
print(cipher_text)
print("-------------------------------------------")
# Decrypt the AES key using RSA private key
decrypted_aes_key = private_key.decrypt(
    cipher_rsa,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decrypt the phone number using the decrypted AES key
decipher_suite = Fernet(decrypted_aes_key)
decrypted_phone_number = decipher_suite.decrypt(cipher_text).decode()
print("-------------------decrypted--------------------")
print(decrypted_phone_number)
print("------------------------------------------")
print("Original Phone Number:", phone_number)
print("Decrypted Phone Number:", decrypted_phone_number)
