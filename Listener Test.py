import socket
import argparse
import time
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="dB", help="dBm")
    args = parser.parse_args()

    colokan = socket.socket()
    colokan.connect(('192.168.43.174',4004))
    print 'Connection established'

    un = colokan.recv(32)
    print un
    pa = colokan.recv(10)
    print pa
    s = 0
    while True:
        ss = args.dB
        ss = (int(ss) + s)
        colokan.send(str(ss))
        print ss
        s = (s + 1) % 10
        time.sleep(0.5)
    colokan.close()

main()

