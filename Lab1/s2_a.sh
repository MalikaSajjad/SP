#!/bin/bash
if [ $# -eq 2 ]
then
	fname=$1
	usrname=$2
	set `ls -il $fname`
	if [ $4 = $usrname ]
	then
		cheating=0
		echo $cheating
	else
		cheating=1
		echo $cheating
	fi
fi 
