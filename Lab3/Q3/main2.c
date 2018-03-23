#include<stdio.h>
#include"myStr.h"

void main ()
{
	char arr[7] = "abcdcba";
	if(isPalindrome(arr, 7) == 1)
		printf("palindrome\n");
	else
		printf("not a palindrome\n");
}
