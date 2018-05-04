#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<fcntl.h>
int main(int argc,char *argv[])
{
	char buff[256];
	if(argc == 3)
	{
		//printf("%s",argv[1]);
		//printf("%s",argv[0]);
		//printf("%s",argv[2]);
		
		int fd = open(argv[1],O_RDONLY);
		if(fd != -1)
		{
			//printf("%s",argv[1]);			
			int fd1 = open(argv[2],O_WRONLY);
			if(fd1 != -1)
			{
				int fdS = read(fd,buff,255);
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
			printf("source file not opened");
	}
	//// for mv
	//remove(argv[1]);

	return 0;
}
