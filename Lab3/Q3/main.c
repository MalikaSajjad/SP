#include<stdio.h>
//#include<conio.h>
#include"myMath.h"

void main()
{
	int n1, n2;	

	printf("enter number : ");
	scanf("%d", &n1);
	printf("enter number : ");
	scanf("%d", &n2);

	if(isEqual(n1, n2) == 1)
		printf("numbers are equal");
	else
		printf("numbers are not equal");

	swap(n1, n2);
	//printf("\nnumbers are swaped, now\nn1 = %d\nn2 = %d\n",n1,n2);
}
