#include<stdio.h>
void rotate(int* nums, int numsSize, int k) {
    int i,j;
    int temp;
    for(i=0;i<k;i++){
        temp=nums[numsSize-1];
        for(j=numsSize-1;j>0;j--){
            nums[j]=nums[j-1]; 
        }
        nums[0]=temp;
}
    return nums;
} 
