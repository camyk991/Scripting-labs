#!/bin/bash


filename=$1
privatekey=$2

if [[ $# -lt 2 ]] ; then
  echo "Usage: sign <file> <private_key>"
  exit 1
fi

openssl dgst -sha256 -sign $privatekey -out /tmp/$filename.sha256 $filename
openssl base64 -in /tmp/$filename.sha256 -out signature.sha256
rm /tmp/$filename.sha256
