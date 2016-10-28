#!/bin/bash
regex=$(cat ./regex)
echo -e "Testing the following bash regex
================================
\v$regex\v
================================"
while read -r line
 do
  if [[ "$line" =~ $regex ]];
   then
    printf '%-25s  \033[0;32m%-10s\033[0m \n' "$line" "MATCHED"
   else
    printf '%-25s  \033[0;31m%-10s\033[0m \n' "$line" "NOT MATCHED"
   fi
 done < ./patterns
