import hashlib
f = open('Wordlist.txt', 'r+')
liste = f.readlines()
hash=input('type hash : ')
for i in range(0,len(liste) + 1):
	if hashlib.sha224(liste[i][0:-1].encode('utf-8')).hexdigest() == hash:
		print("password : " + liste[i])
		exit()
print("no password")
