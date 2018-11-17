#!/bin/bash

cat test test.txt | awk '{ip[$1]++ }END{for (i in ip){print i,ip[i]}}'
echo 

cat test test.txt | awk '{ip[$1]++}END{for (i in ip){if(ip[i] == 1){print i}}}'
