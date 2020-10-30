import os
import sys
import time
import random
import socket



def port_scan(host, startPort, endPort, canshowallports):
	print ("[!!] Started scanning!")
	tcp_scan(host, startPort, endPort, canshowallports)
	print ("[!] Scan on host " + host + " complete")


def tcp_scan(host, startPort, endPort, canshowallports):
	for port in range(startPort, endPort+1):
		tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if (canshowallports == "yes"):
			try:
				tcp.connect((host, port))
				print ("[!!] Found open port " + str(port) + " on host " + host)
				tcp.close()
			except Exception:
				print ("[!!] Found closed/filtered port " + str(port) + " on host " + host)
				tcp.close()
		elif (canshowallports == "no"):
			try:
				tcp.connect((host, port))
				print ("[!!] Found open port " + str(port) + " on host " + host)
				tcp.close()
			except Exception:
				tcp.close()
				pass
		else:
			showUsage()


def clearTerminal():
	if (os.name == "nt"):
		os.system("cls")
	else:
		os.system("clear")

def showHelp():
	clearTerminal()
	print ("Compact way of scanning targets - CompactScanner")
	print ("Usage: ./c_scanner.py [ip] [starting port] [ending port] [show only open ports?]")
	print ("Example: ./c_scanner.py 192.168.1.254 70 90 yes")
	print ("Example: ./c_scanner.py 192.168.1.78 10 100 no")
if (len(sys.argv) == 5):
	hostname = sys.argv[1]
	startPort = sys.argv[2]
	endPort = sys.argv[3]
	canshowallports = sys.argv[4]
	port_scan(hostname, int(startPort), int(endPort), canshowallports)
else:
	showHelp()
