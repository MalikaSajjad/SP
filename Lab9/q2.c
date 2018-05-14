#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<fcntl.h>
int main()
{
	char arr[] = "error\n";	
	char buff[1024];
	int fd = open("/home/malika/SP/Labs/Lab9/f1", O_RDONLY);
	int fd1 = creat("errorAndoutput.txt",0777);
	close(2);
	int n_fd1 = dup(fd1); 
	dup2(fd1, 1); 
	
	
	int n;
	if (fd1 == -1 || fd == -1)
	{
		write(fd1, arr, 7);
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
