#include<stdio.h>
/**int maxSubArray(int* nums, int numsSize) {
    int i,j,k,sum=0;
    int max=nums[0];
    for(i=numsSize;i>0;i--){
    	for(j=0;j<i;j++){
    		sum=0;
    		for(k=j;k<j+numsSize-i+1;k++){
    				sum+=nums[k];
    		}
    		if(sum>max)
    			max=sum;
    	}
    }
    return max;
}**/
int maxSubArray(int* nums, int numsSize) {
    int i,j,thisSum=0,maxSum=nums[0];
    for(i=0;i<numsSize;i++){
        thisSum=0;
        for(j=i;j<numsSize;j++){
            thisSum+=nums[j];
        if(thisSum>maxSum)
			maxSum=thisSum;
        };
    }
    return maxSum;
}
 
int main(void){
	int t;
	int nums[3]={1,2,3};
	t=maxSubArray(nums,3);
	printf("%d\n",t);
} 
