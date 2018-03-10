#!/bin/bash
fname=$1
IFS=$'\n'
counter=1
# writes even number lines in evenfile and odd number in oddfile
for lines in `cat $fname`
do
	if [ $((counter % 2)) -eq 0 ]
	then
		echo $lines 1>>evenfile
		counter=$((counter + 1))		
	else
		echo $lines 1>>oddfile
		counter=$((counter + 1))
		#echo "O:"$counter
		#echo $lines
	fi
done 
