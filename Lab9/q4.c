#include<sys/stat.h>
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<fcntl.h>
int main(int argc, char* argv[])
{
	struct stat buf;
	char* ptr;	
	int i = 1;
	for(i; i < argc; i++)
	{
		stat(argv[i], &buf);		
		printf("%s\n", argv[i]);
		if(S_ISREG(buf.st_mode))
		{ 
			ptr = "is a regular file";
			printf("%s\n", ptr);
			printf("ino # %d", buf.st_ino);
		}
		else if(S_ISDIR(buf.st_mode))
		{ 
			ptr = "is a directory";
		}		
		else
		{
			ptr = "have unknown mode";
			printf("%s\n", ptr);
	
	}	}
	
	return 0;
}
