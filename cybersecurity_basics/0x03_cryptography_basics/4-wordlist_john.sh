#!/bin/bash
john --format=raw-md5 --wordlist=rockyou.txt $1 > 4-password.txt
