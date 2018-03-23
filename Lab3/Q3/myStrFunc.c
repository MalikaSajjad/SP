int isPalindrome(char *arr, int size)
{	
	int a;
	int flag = 0;
	size--;
	for(a = 0; a < size; a++)
	{
		if(arr[a] != arr[size])
		{
			flag = 1;
			break;
		}
		size--;
	}
	if(flag == 0)
		return 1;
	return -1;
}
