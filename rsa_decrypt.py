from sys import argv
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP


# Read our private key
private_key = RSA.import_key(open("private.pem").read())

# Read bytes from file (assumes input is path to file)
if len(argv) > 1:
    with open(argv[1], 'rb') as file:
        data = file.read()

    # Decrypt and print and save to file
    pkey = RSA.importKey(open('private.pem').read())
    cipher2 = PKCS1_OAEP.new(pkey)
    result = cipher2.decrypt(data)
    outfile = open("./keylogger_data.txt", "w")
    outfile.write(result.decode("utf-8"))
    print(result)
