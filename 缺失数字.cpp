#include<stdio.h>
int missingNumber(int* nums, int numsSize) {
    int i,j,t;
    for(i=0;i<numsSize-1;i++){
        for(j=i+1;j<numsSize;j++){
            if(nums[j]<nums[i]){
                t=nums[j];
                nums[j]=nums[i];
                nums[i]=t;
            }
        }
    }
    for(i=0;i<numsSize;i++){
        if(nums[i]!=i)
            break;
    }
    printf("%d\n",i);//return i;
}
int main(void){
	int s[5]={0,2,4,1,5};
	missingNumber(s,5);
}
 
