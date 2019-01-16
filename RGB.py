import socket
import time
import subprocess
import threading

def spam(x):
    while True:
        res = subprocess.Popen("iw dev rename%s link"  %(x + 4), shell=True, stdout=subprocess.PIPE)
        print res
        sign = 0
        for line in res.stdout:
            if 'Signal' in line:
                sign = line.strip('\n')
                #val = lin[44:46]
                print str(sign)
            else:
                colokan.send('Connection interrupted')


        ss = str(sign) + ';' + str(x)
        colokan.send(ss)
        print ss

        time.sleep(0.2)


class user(threading.Thread):
    def __init__(self, uname, pasw, num):
        threading.Thread.__init__(self)
        self.user = uname
        self.pasw = pasw
        self.num = num

    def run(self):
        subprocess.Popen("iw dev wlan0 interface add wlan%s type station"  %(self.num + 1), shell=True, stdout=subprocess.PIPE)
        subprocess.Popen("ifconfig rename%s down"  %(self.num + 4), shell=True, stdout=subprocess.PIPE)
        subprocess.Popen("if link set dev rename%(1)s address EA:EA:EA:EA:EA:E%(2)s"  % {"1" : str(self.num + 4), "2" : str(self.num)}, shell=True, stdout=subprocess.PIPE)
        subprocess.Popen("ifconfig rename%s down"  %(self.num + 4), shell=True, stdout=subprocess.PIPE)
        z = threading.Thread(subprocess.Popen("wpa_supplicant -D nl80211,wext -i rename%(1)s -c <(wpa_passphrase \"%(2)s\" \"%(3)s\")"  % {"1" : str(self.num + 4), "2" : self.uname, "3" : self.pasw}, shell=True, stdout=subprocess.PIPE))
        z.start()

        spam(self.num)

while True:
    try:
        print 'Connecting to 192.168.43.174...'
        colokan = socket.socket()
        colokan.connect(('192.168.43.174',4004))
        print 'Connection established'
        break
    except:
        continue

use = []
x = 0

while True:
    usern = colokan.recv(32)
    print usern
    passw = colokan.recv(10)
    print passw
    use[x] = user(usern, passw, x)
    use[x].start()
    x += 1








