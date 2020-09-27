from cryptography.fernet import Fernet
import os
import sys
files = sys.argv[1]

file = open('key.key','rb')
key = file.read()
file.close

os.chdir("/home/sanveer/crypto_service/cryptoProject/toDecrypt") 

with open(files,'rb') as f:
	data = f.read()

fernet = Fernet(key)
decrypted = fernet.decrypt(data)

name_decrypt = files+'.decrypted'
#write encrypted file
with open(name_decrypt, 'wb') as f:
	f.write(decrypted)
