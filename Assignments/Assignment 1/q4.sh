#!/bin/bash
# remove identical lines from file
read -p "enter file name :" fname
sort "${fname}" | uniq 1>"$fname"

