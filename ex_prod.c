void ex_product3(int *list,int len)	{
	int i = 0,p = 1;
	
	int *result = (int*)calloc(len,sizeof(int));
	
	result[0] = 1;
	for(i = 1 ; i<len ; i++)
		result[i] = result[i-1] * list[i-1];
	
	for(i = len - 2 ; i>= 0 ; i--){
		p = p * list[i+1];
		result[i] = result[i] * p;
	}
	
	printf("\n\n\n");
	for(i = 0 ; i< len ; i++)
		printf("%d, ",result[i]);
		
	
}
