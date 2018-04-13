#!/bin/bash
if [ $# -eq 1 ]
then
	pname=$1
	PID=`pidof $pname`
	cd /proc/$PID
	set `head status`
	
	echo "PID:" ${PID}
	echo "Name:" ${pname}
	echo "state:" $4 $5
	shift 5
	echo "PPID:" $8
	
else
	echo "process name is missing"
fi
