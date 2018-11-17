#!/bin/bash 

for i in `ls *.py` 
do
  x=`head -1  $i`
  chmod +x $i
  if ! [ "${x:0:2}" == "#!" ]
  then
#       sed -i '1d'  $i 
      sed -i '1i #!/usr/bin/env python3'  $i
  fi 
done
  
