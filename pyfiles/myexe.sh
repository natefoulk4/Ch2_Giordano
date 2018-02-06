#!/bin/bash

counter=1
while [ $counter -le $1 ]
do
    python driver.py 700 $counter 0.1 3
    ((counter++))
done



     
