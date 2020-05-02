from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

pubkey = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA95UUVFbx17//PAKDAt2U' \
         b'\nX3eRxdobjR3GWs6KNLWKfkgJRjux8y3eoYZpugZHYyDptN0VjbxjrkOWhubDVeCv' \
         b'\nCHSBI7FUzf62bc5048zaifHFLQFselSD6zonc2p9w4oOjqmZj3POXEmB//mOXNFi' \
         b'\n8b0o5HYQWB084H3MgtijZBCMVLikbLrGYmpbUZatiHb48f5w2mNeUihDK9THsvf+\n3pk2Kp6e3VsMgaAtHztvt7NVKyPphtcYS' \
         b'/UTu1W/qIvTPWr2/utwsffo78o4e+SJ\n+zbMqbgAJieIv9cFFfebr3QNxQ4aDz5tO8YKLLfWqQBN9aoxUM2I8gBVbl378Vnk' \
         b'\nIwIDAQAB\n-----END PUBLIC KEY----- '

message = 'test'
message = message.encode()
# key = RSA.importKey(open('receiver.pem').read())
key = RSA.importKey(pubkey)
cipher = PKCS1_OAEP.new(key)
c = cipher.encrypt(message)
print(c)

pkey = RSA.importKey(open('private.pem').read())
cipher2 = PKCS1_OAEP.new(pkey)
print(cipher2.decrypt(c))

