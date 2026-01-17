#!/bin/bash
curl -X PUT -H "Host: $1" -d "$3" "$2"
