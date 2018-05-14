#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<fcntl.h>
int main()
{
	char buff[1024];
	int fd1 = open("/etc/passwd", O_RDONLY);
	//printf("fd1 %d", fd1);
	int fd2 = dup(fd1);
	//printf("fd2 %d", fd2);
	int n;
	for(;;)
	{
		n = read(fd2,buff,1024);
		if(n <= 0)
		{
			close(fd1);
			close(fd2);
			return 0;
		}
		write(1, buff, n);
	}
	
	return 0;
}
