import hashlib
f = open('Wordlist.txt', 'r+')
liste = f.readlines()
print("\033[31m  _   _                 _       _                     _   ")
print("\033[31m | | | |   __ _   ___  | |__   | | __  _ __    __ _  | | __")
print("\033[31m | |_| |  / _` | / __| | '_ \  | |/ / | '__|  / _` | | |/ /")
print("\033[31m |  _  | | (_| | \__ \ | | | | |   <  | |    | (_| | |   < ")
print("\033[31m |_| |_|  \__,_| |___/ |_| |_| |_|\_\ |_|     \__,_| |_|\_\ ")
print("\033[31m ")
hash=input('type hash : ')
for i in range(0,len(liste) + 1):
	if hashlib.sha224(liste[i][0:-1].encode('utf-8')).hexdigest() == hash:
		print("password : " + liste[i])
		exit()
print("no password")
