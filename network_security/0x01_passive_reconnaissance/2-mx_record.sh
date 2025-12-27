#!/bin/bash
^nslookup\s+(-q|-type|-querytype|-query)=?[mM][xX]\s+\$1
nslookup -type=mx "$1"
