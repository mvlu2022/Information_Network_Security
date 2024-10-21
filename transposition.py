def transpose(text, key):
    columns = [''] * key
    for i, char in enumerate(text):
        columns[i % key] += char
    return ''.join(columns)

def decrypt(ciphertext, key):
    rows = len(ciphertext) // key + (len(ciphertext) % key > 0)
    columns = [''] * key
    for i in range(key):
        columns[i] = ciphertext[i * rows: (i + 1) * rows]
    plaintext = ''
    for i in range(rows):
        for j in range(key):
            if i < len(columns[j]):
                plaintext += columns[j][i]
    return plaintext

key = 4
plaintext = input("Please give Your Plain Text for Encryption: ")
ciphertext = transpose(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print("Encrypted:", ciphertext)
print("Decrypted:", decrypted_text)