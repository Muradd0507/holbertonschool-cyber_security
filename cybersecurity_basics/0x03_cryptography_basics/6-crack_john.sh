#!/bin/bash
john --format=raw-sha256 $1 --wordlist=/usr/share/wordlists/rockyou.txt
