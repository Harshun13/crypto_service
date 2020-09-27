from cryptography.fernet import Fernet
import os
import sys
files = sys.argv[1]

file = open('key.key','rb')
key = file.read()
file.close

os.chdir("/home/sanveer/crypto_service/cryptoProject/toCrypt") 

with open(files,'rb') as f:
	data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

name_encrypt = files+'.encrypted'
#write encrypted file

with open(name_encrypt, 'wb') as f:
	f.write(encrypted)
