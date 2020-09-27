#!/bin/bash

cd /home/sanveer/crypto_service/cryptoProject/toDecrypt
array=($(echo *))

cd /home/sanveer/crypto_service/decrypted
de_crypted="$(echo *)"

for files in ${array[*]}
do 
	if [[ "de_crypted" == "files.decrypted" ]]
	then
		echo "present $files"
	else 
		cd /home/sanveer/crypto_service
		python3 decrypt.py "$files"
		mv ~/crypto_service/cryptoProject/toDecrypt/"$files.decrypted" ~/crypto_service/decrypted/"$files.decrypted"
	fi
done
