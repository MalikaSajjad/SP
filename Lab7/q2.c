#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<fcntl.h>
int main(int argc,char *argv[])
{
	char buff[4096];	
	if (argc == 2)
	{
		int fd = open("/etc/shadow",O_RDONLY,0777);
		if(fd != -1)
		{
			int fd1 = open(argv[1],O_WRONLY);			
			if(fd1 != -1)
			{
				int fdS = read(fd,buff,4096);
				if(fdS != -1)
				{
					int fdD = write(fd1, buff, fdS);
					if(fdD == -1)
					{
						printf("file not write");
					}
				}
				else
					printf("file not read");
				
			}
			else
			{
				printf("destination file not opened");
			}
		}
		else
			printf("src file not opened");	
		
	}
	else
		printf("inappropriate args");


	return 0;
}
