#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<fcntl.h>
int main()
{
	char arr[] = "error \n";	
	char buff[1024];
	int fd1 = open("/home/malika/SP/Labs/Lab9/f2.txt", O_RDONLY);
	int fd = open("f1.txt", O_WRONLY);
	dup2(fd1, 1);
	//dup2(fd1, 2);
	dup2(fd, 0);
	
	int n;
	if (fd == -1 || fd1 == -1)
	{
		write(2, arr, 8);
	}
	else
	{	
		for(;;)
		{		
			n = read(fd,buff,1024);
			if(n <= 0)
			{
				close(fd);
				close(fd1);
				return 0;
			}
			write(fd1, buff, n);
		}
	}
	
	
	


	return 0;
}
