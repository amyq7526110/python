for i  in  ` ls . `
   do
    if [   -f   $i   ];then
   
      

      if  grep   -q  "$1"  $i ;then 
      echo   $i
    fi
    
   else 
  break
  fi
done   
