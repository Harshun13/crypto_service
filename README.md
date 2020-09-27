# crypto_service
key.py = generates key to encryp files

encrypt.py = codes that encrypt a text files into an encrypted text files

decrypt.py = codes that decrpyt the encrypted text files into text files

crypt.sh = codes that check that there is a file or a text file in tocrypt folder,
if there is a text file in tocrypt folder, crypt.sh makes the the text file into encrypted text file 
by calling encrypt.py.
After encrypted the text file, it makes a copy of the encrypted files in the crypted folder.

crypt.service = the service 

decrypt.sh = codes that check that there is a file or a text file in toDecrypt folder,
if there is a encrypted text file in toDecrypt folder, decrypt.sh makes the the encrypted text file into decrypted text file 
by calling decrypt.py.
After decrypted the text file, it makes a copy of the decrypted files in the decrypted folder.


