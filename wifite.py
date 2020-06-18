#!/bin/python3

import os

try:
	sources = "\ndeb http://kali.cs.nctu.edu.tw/ /kali main contrib non-free\ndeb http://kali.cs.nctu.edu.tw/ /wheezy main contrib non-free\ndeb http://kali.cs.nctu.edu.tw/kali kali-dev main contrib non-free\ndeb http://kali.cs.nctu.edu.tw/kali kali-dev main/debian-installer\ndeb-src http://kali.cs.nctu.edu.tw/kali kali-dev main contrib non-free\ndeb http://kali.cs.nctu.edu.tw/kali kali main contrib non-free\ndeb http://kali.cs.nctu.edu.tw/kali kali-bleeding-edge main"

	print("-"*50)
	print("Wifite downloader has started")
	print("-"*50)

	#Write sources to sources.list
	f = open("/etc/apt/sources.list", "r")
	if f.mode == 'r':
		if not(sources in f.read()):
			print("\x1b[0;31;40m" + "Sources not present, adding sources" + "\x1b[0")
			fs = open("/etc/apt/sources.list", "a+")
			fs.write(sources)
		else:
			print("\x1b[0;32;40m" + "Sources present, resuming process" + "\x1b[0")

	#Installing libs and Pyrit, HCX
	os.system("sudo apt update")
	os.system("sudo apt install python-dev -y")
	os.system("sudo apt install python3-dev -y")
	os.system("sudo apt install libssl-dev -y")
	os.system("sudo apt install libpcap-dev -y")
	os.system("sudo apt install libcurl4-gnutls-dev -y")
	os.system("sudo git clone https://github.com/JPaulMora/Pyrit")
	os.system("sudo git clone https://github.com/ZerBea/hcxdumptool")
	os.system("sudo git clone https://github.com/ZerBea/hcxtools")
	os.chdir("Pyrit")
	os.system("sudo python setup.py clean")
	os.system("sudo python setup.py build")
	os.system("sudo python setup.py install")
	os.chdir("../hcxdumptool")
	os.system("sudo make")
	os.system("sudo make install")
	os.chdir("../hcxtools")
	os.system("sudo make")
	os.system("sudo make install")
	print("-"*50)
	print("Done")
	print("-"*50)

except KeyboardInterrupt:
	print("Canceled")
