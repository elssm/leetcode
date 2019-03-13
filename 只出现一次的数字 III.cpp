#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int* singleNumber(int* nums, int numsSize, int* returnSize) {
    int i,j;
    int c,b=0;
    int *ret=(int *)malloc(sizeof(int)*((*returnSize)=2));
    for(i=0;i<numsSize;i++){
    	c=0;
    	for(j=0;j<numsSize;j++){
    		if(nums[j]==nums[i])
    			c++;
    	}
    	if(c==1)
    		ret[b++]=nums[i];
    }
    for(i=0;i<b;i++)
    	printf("%3d",ret[i]);
}
int main(void){
	int t;
	int s[6]={1,2,1,3,2,5};
	singleNumber(s,6,&t);
} 
