#!/bin/bash

openssl enc -aes-256-cbc -salt -pbkdf2 -iter 10000 -in "$1" -out "output.txt" -k "$2"


