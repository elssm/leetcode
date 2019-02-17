#include<stdio.h>
int maximumProduct(int* nums, int numsSize) {
    int i,j,t,a,b;
    for(i=0;i<numsSize-1;i++){
        for(j=i+1;j<numsSize;j++){
            if(nums[i]<nums[j]){
                t=nums[j];
                nums[j]=nums[i];
                nums[i]=t;
            }
        }
    }
    a=nums[0]*nums[1]*nums[2];
    b=nums[0]*nums[numsSize-1]*nums[numsSize-2];
    return a>b?a:b;
}
int main(void){
	int s[5]={-4,-3,-2,-1,60};
	int t;
	t=maximumProduct(s,5);
	printf("%d\n",t);
} 
