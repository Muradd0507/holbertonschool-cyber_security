#!/bin/bash
addgroup $2
chgrp $1 $2
chmod g+rx $1
