#!/bin/bash
sudo curl -X GET -H "Host: $1" -d "$3" "$2"
