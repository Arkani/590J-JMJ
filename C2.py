import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "127.0.0.1" #localhost
port = 10101
addr = (ip, port)

commands = ["start", "stop"]

while True:
    cmd = input("cmd>")
    print(cmd)
    if cmd in commands:
        sock.sendto(cmd.encode(), addr)
    else:
        exit()
