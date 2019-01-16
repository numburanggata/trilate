import socket
import subprocess
import argparse
import MySQLdb

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument(dest="intr", help="Wireless LAN interface")
	parser.add_argument(dest="malis", help="IP address of the main listener")
	args = parser.parse_args()
	malis = '192.168.43.174'
    colokan = socket.socket()
    colokan.connect((malis,4004))
    print ('Connection established: ' + malis + '\t' + str(4004))

	un = colokan.recv(32)
	print un
	pa = colokan.recv(10)
	print pa
	while True:
		getss(args.intr, colokan)
	
def getss(interface, conn):
    rea = subprocess.Popen("iwconfig %s"  % interface, shell=True, stdout=subprocess.PIPE)
    for line in rea.stdout:
        if 'Signal' in line:
            lin = line.strip('\n')
            ss = lin[44:46]
			colokan.send(ss)
			time.sleep(0.5)
			
            print ss

main()

