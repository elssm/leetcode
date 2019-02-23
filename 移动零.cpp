#include<stdio.h>
void moveZeroes(int* nums, int numsSize) {
    int i,temp,t,count=0;
    t=numsSize;
    while(count<numsSize){
        if(nums[count]==0){
            temp=nums[count];
            for(i=count;i<numsSize-1;i++)
                nums[i]=nums[i+1];
            nums[numsSize-1]=temp;
            numsSize--;
        }
        else
            count++;
    }
    
   /** void moveZeroes(int* nums, int numsSize) {
    int i = 0,j = 0;
    for(i = 0 ; i < numsSize; i++)		//别人的方法，感觉很好 
    {
        if(nums[i] != 0)
        {
            nums[j++] = nums[i];
        }
    }
    while(j < numsSize)
    {
        nums[j++] = 0;
    }
} **/
    
    for(i=0;i<t;i++)
    	printf("%3d",nums[i]);
    //return nums;
}
int main(void){
	int s[5]={0,1,0,2,3};
	moveZeroes(s,5);
} 
