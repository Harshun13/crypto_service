from cryptography.fernet import Fernet

file = open('key.key','rb')
key = file.read()
file.close

with open('test.txt.encrypted','rb') as f:
	data = f.read()

fernet = Fernet(key)
decrypted = fernet.decrypt(data)

#write encrypted file

with open( 'test.txt.decrypted', 'wb') as f:
	f.write(decrypted)
