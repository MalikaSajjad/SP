#include<stdio.h>
#include"myStr.h"
#include"myMath.h"
void main()
{
	int n1, n2;	
	char arr[7] = "abcdcba";
	printf("enter number : ");
	scanf("%d", &n1);
	printf("enter number : ");
	scanf("%d", &n2);

	if(isEqual(n1, n2) == 1)
		printf("numbers are equal\n");
	else
		printf("numbers are not equal\n");

	swap(n1, n2);
	//printf("\nnumbers are swaped, now\nn1 = %d\nn2 = %d\n",n1,n2);
	if(isPalindrome(arr, 7) == 1)
		printf("palindrome\n");
	else
		printf("not a palindrome\n");
}
