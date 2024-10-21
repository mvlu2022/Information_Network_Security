import random
import string

def generate_key():
    alphabet = list(string.ascii_lowercase)
    shuffled_alphabet = alphabet[:]
    random.shuffle(shuffled_alphabet)
    return ''.join(shuffled_alphabet)

def substitute(text, key):
    alphabet = string.ascii_lowercase
    cipher = str.maketrans(alphabet, key)
    return text.lower().translate(cipher)

def decrypt(ciphertext, key):
    alphabet = string.ascii_lowercase
    cipher = str.maketrans(key, alphabet)
    return ciphertext.translate(cipher)
key = generate_key()
plaintext =input("Please give your Plain text for encryption: ")
ciphertext = substitute(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print("Key:", key)
print("Encrypted:", ciphertext)
print("Decrypted:", decrypted_text)