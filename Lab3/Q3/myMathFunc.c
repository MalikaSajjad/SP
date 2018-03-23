int isEqual(int n1, int n2)
{
	if(n1 == n2)
		return 1;
	else
		return -1;
}
void swap(int n1, int n2)
{
	n2 = n1 + n2;
	n1 = n2 - n1;
	n2 = n2 - n1;
	
}
