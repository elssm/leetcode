#include<stdio.h>
int thirdMax(int* nums, int numsSize) {
	int first=0,second=0,third=0; //假设所有值都大于0 
    //long first = LONG_MIN,second = LONG_MIN,third = LONG_MIN;
    int i;
    for(i = 0;i < numsSize;i++)
        if(nums[i] > first)
            first = nums[i];
    for(i = 0;i < numsSize;i++)
        if(nums[i] > second && nums[i] != first)
            second = nums[i];
    for(i = 0;i < numsSize;i++)
        if(nums[i] > third && nums[i] != first && nums[i] != second)
            third =nums[i];
    if(third != 0)
        return third;
    else  return first;
}
int main(void){
	int s[5]={1,2,4,3,5};
	int t;
	t=thirdMax(s,5);
	printf("%d\n",t);
} 
