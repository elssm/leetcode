#include<stdio.h>
int searchInsert(int* nums, int numsSize, int target) {
    int i=0;
    while(i<numsSize){
        if(nums[i]<target)
            i++;
        else
            return i;
    }
    return i;
}
int main(void){
	int s;
	int nums[5]={1,2,3,4,5};
	s=searchInsert(nums,5,6);
	printf("%d\n",s);
} 
