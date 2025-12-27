#!/bin/bash
subfinder -d "$1" -silent | while read h; do ip=$(dig +short "$h" | head -n1); [ -n "$ip" ] && echo "$h,$ip"; done | tee "$1.txt"
