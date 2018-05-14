#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<fcntl.h>
int main(int argc, char* argv[])
{
	if (argc != 2)
	{
		fprintf(stderr, "incorrect # of args\n");
		exit(1);
	}	
	if(access(argv[1], R_OK) == 0)
		printf("you have read access to this file\n");	
	else
		printf("you do not have read access to this file\n");
	if(access(argv[1], W_OK) == 0)
		printf("you have write access to this file\n");	
	else
		printf("you do not have write access to this file\n");
	if(access(argv[1], X_OK) == 0)
		printf("you have execute access to this file\n");	
	else
		printf("you do not have execute access to this file\n");



	return 0;
}
