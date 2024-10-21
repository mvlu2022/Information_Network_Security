from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

message = b"Hello, this is a test message"

h = SHA256.new(message)

signature = pkcs1_15.new(key).sign(h)

try:
    pkcs1_15.new(key.publickey()).verify(h, signature)
    print("Signature is valid.")
    print(message)
except (ValueError, TypeError):

    print("Signature is invalid.")
    print("we can't get your message")
