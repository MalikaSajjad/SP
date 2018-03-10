#!bin/bash
declare -A dict

# create dict with keys as extensions
for i in `ls *.*`	# i will have file name e.g abc.c
do
	extension="${i##*.}"
	dict[${extension}]=${i}	
done	

#make directories of dict keys - extionsions
for keys in ${!dict[@]} # shows keys
do
	mkdir ${keys} 2>err
done

# move files with same extension in one folder
for i in `ls *.*`	
do	
	extension="${i##*.}"
	mv ${i} ${extension}	
done
