#!/bin/bash
Is_lower()
{
	string=$1	
	echo "${string,,}"
}

Is_root()
{
	if [ `whoami` != "root" ]
	then
		return 0
	else
		return 1

	fi
}

Is_user_exists()
{
	uname=$1
	IFS=$'\n'	
	for line in `cat /etc/passwd`
	do				
		IFS=$':'
		for u in $line
		do		
			if [ $uname = $u ]
			then				
				return 1
			else
				break
			fi	
			
			return 0
		done
		IFS=$'\n'
	done
}

# fucn call
Is_lower GREEDY

# func call
Is_root
if [ "$?" -eq 0 ]
then 
	echo "False"
else
	echo "True"
fi

# # #
read -p "Enter user name" us
Is_user_exists $us
if [ "$?" -eq 0 ]
then 
	echo "False"
else
	echo "True"
fi


