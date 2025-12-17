#!/bin/bash
ps -u "$1" -o pid,user,vsz,rss,cmd --sort=pid | grep -v " 0  0 "
