#!/bin/bash
grep -o '[[:alnum:]]' /dev/urandom | head -c "$1"
