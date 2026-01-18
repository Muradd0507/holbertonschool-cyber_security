#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
    exit 1
fi

# Remove the {xor} prefix if it exists
encoded_string="${1#\{xor\}}"

# 1. Decode from Base64
# 2. Convert to a stream of decimal bytes
# 3. XOR each byte with 95 (the '_' character)
# 4. Convert back to ASCII characters
echo "$encoded_string" | base64 -d | perl -pe 's/(.)/chr(ord($1) ^ 95)/ge'
echo ""
