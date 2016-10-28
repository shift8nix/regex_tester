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
    printf '\033[0;32m%-6s\033[0m %s\n' "MATCH" "$line" 
   else
    printf '\033[0;31m%-6s\033[0m %s\n' "FAIL" "$line"
   fi
 done < ./patterns
