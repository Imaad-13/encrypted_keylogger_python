from cryptography.fernet import Fernet

# Generate key once
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)

# Encrypt the log
def encrypt_log():
    with open("key.key", "rb") as f:
        key = f.read()

    fernet = Fernet(key)

    with open("log.txt", "rb") as f:
        original = f.read()

    encrypted = fernet.encrypt(original)

    with open("log_encrypted.txt", "wb") as f:
        f.write(encrypted)

if __name__ == "__main__":
    generate_key()   # Run this only once
    encrypt_log()
