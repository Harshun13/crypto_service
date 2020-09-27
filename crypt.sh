#!/bin/bash

cd /home/sanveer/crypto_service/cryptoProject/toCrypt
array=($(echo *))

cd /home/sanveer/crypto_service/cryptoProject/crypted
in_crypted="$(echo *)"

for files in ${array[*]}
do 
	if [[ "in_crypted" == "files.encrypted" ]]
	then
		echo "present $files"
	else 
		cd /home/sanveer/crypto_service
		python3 encrypt.py "$files"
		mv ~/crypto_service/cryptoProject/toCrypt/"$files.encrypted" ~/crypto_service/cryptoProject/crypted/"$files.encrypted"
	fi
done
