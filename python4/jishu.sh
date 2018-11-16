#!/bin/bash 

  E_NOARGS=65
  
  E_Baddir=66

  nowtime=`date +%F` 
 
  if [ $# -ne 1  ]

  then 

      echo "Usage: `basename  $0 ` directory name"

      exit $E_NOARGS

  fi 
 
  if [ ! -d "$1" ] 
  
  then 

       echo "Not exist directory !"

       exit $E_Baddir
  fi  
  
  cd $1
  
  
  for i  in  "$PWD/*.py"

  do

     let "sum = sum +  `grep -Pv '^(#|$)' $i | wc -l`"

  done

  : ${sum:-0}

  echo $sum

  echo  -e "$nowtime\t$PWD\t$sum" >> /var/log/pyhangshu.log

  exit 0
   

