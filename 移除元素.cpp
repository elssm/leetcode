#include<stdio.h>
int removeElement(int *nums, int numsSize, int val) {
    int i,k;
    for(i=0;i<numsSize;){
        if(val==nums[i]){
            for(k=i;k<numsSize-1;k++)
                nums[k]=nums[k+1];
            numsSize--;
        }
        else
            i++;
    }
    return numsSize;
}
int main(void){
	int i,len;
	int nums[10]={1,2,3,4,5,5,6,7,8,5};
	len=removeElement(nums,10,5);
	for(i=0;i<len;i++){
		printf("%3d",nums[i]);
	}
} 
