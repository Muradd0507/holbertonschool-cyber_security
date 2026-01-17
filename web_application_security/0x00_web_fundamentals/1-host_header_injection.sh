#!/bin/bash
curl -X GET -H "Host: $1" -d "$3" "$2"
