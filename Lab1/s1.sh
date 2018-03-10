read -p "enter 1st number : " num1
read -p "enter 2nd number : " num2
sum=$((num1 + num2))
echo "sum is : ""$sum"
sub=$((num1 - num2))
echo "sub is : ""$sub"
mul=$((num1 * num2))
echo "mul is : "$mul
if [ $num2 -eq 0 ]
then
	echo "div is undefined"
else
	div=$((num1 / num2))
	echo "div is : "$div
	mod=$((num1 % num2))
	echo "mod is : "$mod
fi
