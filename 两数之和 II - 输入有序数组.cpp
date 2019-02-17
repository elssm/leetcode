#include<stdio.h>
#include<stdlib.h>
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int a[2]={0};
    

	for (int i = 0; i < numbersSize - 1; i++)
	{
		for (int j = i+1; j < numbersSize; j++)
		{
			if (numbers[i] + numbers[j] == target)
			{
				//a[0] = i;
				//a[1] = j;
				//return a;
                *returnSize=2;
                int *index=(int*)malloc(2*sizeof(int));
                index[0]=i+1;
                index[1]=j+1;
                return index;
			}
		}
	}
	return 0;
} 
