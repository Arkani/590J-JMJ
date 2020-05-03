import socket
from requests import get

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
            print(msg)
    else:
        exit()
