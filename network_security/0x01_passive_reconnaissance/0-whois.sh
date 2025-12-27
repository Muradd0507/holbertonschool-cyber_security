#!/bin/bash
whois "$1" | awk '
/^(Registrant|Admin|Tech)/{s=$1}
/:/{
  f=$1; sub(/^[^:]+: */,"")
  if(f=="Street") print s" Street,"$0" "
  else if(f=="Phone"||f=="Fax") print s" "f","$0
  else if(f=="Ext") print s" "p" Ext:,"
  else print s" "f","$0
  p=f
}
' > "$1.csv"
