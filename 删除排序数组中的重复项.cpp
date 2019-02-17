#include<stdio.h>
int removeDuplicates(int* nums, int numsSize) {
    int i,j,k;
    for(i=0,j=1;j<numsSize;){
        if(nums[j]==nums[i]){
            for(k=i;k<numsSize-1;k++){
                nums[k]=nums[k+1];
            }
            numsSize--;
        }
        else{
            i++;
            j++;
        }
    }
    return numsSize;
}
int main(void){
	int nums[5]={0,1,1,2,2};
	int i;
	int len;
	len=removeDuplicates(nums,5);
	for(i=0;i<len;i++){
		printf("%3d",nums[i]);
	}
}


