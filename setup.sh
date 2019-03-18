#!/bin/bash
result=`cat ~/.bash_profile | grep "alias slop=\"~/slopify/slopify.py\""`
echo $result
if [ "$result" ]; then
  echo "already set up"
else
  echo "setting up"
  echo "alias slop=\"~/slopify/slopify.py\"" >> ~/.bash_profile
  . ~/.bash_profile
fi
