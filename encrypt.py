from cryptography.fernet import Fernet

file = open('key.key','rb')
key = file.read()
file.close

with open('test.txt','rb') as f:
	data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

#write encrypted file

with open( 'test.txt.encrypted', 'wb') as f:
	f.write(encrypted)
