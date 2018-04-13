if [ $# -eq 1 ]
then
	IFS=$'\n'	
	array=(`cat $1`) 2>error
	if [ $? -eq 0 ]
	then
		echo "length of array : ${#array[*]}"
		echo "contents of array: ${array[*]}"
		echo "length of contents at 3rd index : ${#array[3]}"
	fi
else
	echo "file name missing"
fi


