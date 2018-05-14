#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<fcntl.h>
int main()
{
	char arr[] = "error in 0 < f2.txt \n";	
	char buff[1024];
	int fd = open("/home/malika/SP/Labs/Lab9/f2.txtw", O_RDONLY);
	int fd1 = open("f1.txt", O_WRONLY);
	dup2(fd1, 1);
	dup2(fd1, 2);
	dup2(fd, 0);
	
	int n;
	if (fd == -1)
	{
		write(fd1, arr, 22);
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
