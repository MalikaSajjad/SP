#!/bin/bash
UNIX=('Debian' 'Red hat' 'Ubuntu' 'Suse' 'Fedora')
echo "printing whole array w//o loop : ${UNIX[@]}"
echo "length of array : ${#UNIX[@]}"
echo "length of element on 2nd index : ${#UNIX[2]}"
echo "extracting 2 elements from position 3 : ${UNIX[@]:3:4}"
echo "searching for ubuntu : ${UNIX[@]/Ubuntu/SCOUnix}"
UNIX[5]='AIX'
UNIX[6]='HP-UX'
#echo "printing whole array w//o loop : ${UNIX[@]}"
unset UNIX[2]
#echo ${UNIX[@]}
LINUX=${UNIX[@]}
echo "printing linux: ${LINUX[@]}"
BASH=(${LINUX[@]} ${UNIX[@]})
echo "printing bash : ${BASH[@]}"
unset LINUX
unset UNIX[@]
echo ${UNIX[@]}
echo ${LINUX[@]}
