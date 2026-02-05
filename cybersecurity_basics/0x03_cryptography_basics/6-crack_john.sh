#!/bin/bash
john --format=Raw-sha256 --wordlist=/usr/share/wordlists/rockyou.txt $1
