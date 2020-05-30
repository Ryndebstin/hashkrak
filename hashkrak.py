import hashlib
f = open('Wordlist.txt', 'r+')
liste = f.readlines()
print("  _   _                 _       _                     _   ")
print(" | | | |   __ _   ___  | |__   | | __  _ __    __ _  | | __")
print(" | |_| |  / _` | / __| | '_ \  | |/ / | '__|  / _` | | |/ /")
print(" |  _  | | (_| | \__ \ | | | | |   <  | |    | (_| | |   < ")
print(" |_| |_|  \__,_| |___/ |_| |_| |_|\_\ |_|     \__,_| |_|\_\ ")
print(" ")
hash=input('type hash : ')
for i in range(0,len(liste) + 1):
	if hashlib.sha224(liste[i][0:-1].encode('utf-8')).hexdigest() == hash:
		print("password : " + liste[i])
		exit()
print("no password")
