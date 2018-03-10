#!bin/bash
table()
{
	if [ $# -eq 1 ]
	then
		num=$1	
		for i in `seq 1 10`
		do
			mul=`expr $i \* $num`
			echo "$num x $i = "$mul
		done
	elif [ $# -eq 3 ]
	then
		if [ $3 = "s" ]
		then		
			num=$1	
			for i in `seq $2 10`
			do
				mul=`expr $i \* $num`
				echo "$num x $i = "$mul
			done
		else
			num=$1	
			for i in `seq 1 $2`
			do
				mul=`expr $i \* $num`
				echo "$num x $i = "$mul
			done
		fi
	elif [ $# -eq 4 -a $4 = "se" ]
	then
		num=$1
		for i in `seq $2 $3`
		do
			mul=`expr $i \* $num`
			echo "$num x $i = "$mul
		done
	elif [ $# -eq 4 -a $4 = "r" ]
	then
		num=$1
		i=$2
		while [ $i -gt $3 ]
		do
			mul=`expr $i \* $num`
			echo "$num x $i = "$mul
			i=`expr $i - 1`
			
		done
		
	fi
	
}
if [ $# -eq 0 ]			
then  
	echo "no arg is provided"
elif [ $# -gt 6 ]
then
	echo "more than 6 args are provided"
elif [ $# -eq 1 ]
then 	
	table $1
elif [ $2 = "-s" -a  $4 = "-e" -a $6 = "-r" ]
then
	table $1 $5 $3 r
elif [ $2 = "-s" -a  $4 = "-e"  ]
then
	table $1 $3 $5 se
elif [ $2 = "-s" ]
then
	table $1 $3 s
elif [ $2 = "-e" ]
then
	table $1 $3 e

	
	
fi

