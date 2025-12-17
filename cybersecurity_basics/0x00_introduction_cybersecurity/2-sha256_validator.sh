#!/bin/bash
echo "$2  $1" | sha256sum -c --status && echo "ok"
