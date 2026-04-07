#Packages
from cryptography.fernet import Fernet
import rsa



message = "Secret Message"
print("Original message:", message)


print("-" * 10)


# Symmetric 
print("SYMMETRIC")
symmetric_key = Fernet.generate_key()                   
print("Symmetric Key:", symmetric_key.decode())

fernet = Fernet(symmetric_key)
encrypted_sym = fernet.encrypt(message.encode())   
print("Encrypted (Symmetric):", encrypted_sym)

decrypted_sym = fernet.decrypt(encrypted_sym).decode()  
print("Decrypted (Symmetric):", decrypted_sym)

print("-" * 10)


# ASYMMETRIC 
print("ASYMMETRIC")
public_key, private_key = rsa.newkeys(512)         


print("\nPublic Key:")
print(public_key)


print("\nPrivate Key:")
print(private_key)


encrypted_a = rsa.encrypt(message.encode(), public_key)   
print("\nEncrypted (Asymmetric):", encrypted_a)


decrypted_a = rsa.decrypt(encrypted_a, private_key).decode()  
print("Decrypted (Asymmetric):", decrypted_a)