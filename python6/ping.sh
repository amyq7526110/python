#!/bin/bash

date 
for ip in 176.121.207.{1..254}
do
   ping -c 2  -i0.2  -W1  $ip &> /dev/null
   if [ $? -eq 0 ]
   then
       echo "$ip up"
   else 
       echo "$ip down"
   fi    
done   
date 
