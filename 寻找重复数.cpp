#include<stdio.h>
int findDuplicate(int* nums, int numsSize) {
    int i,j,c;
    for(i=0;i<numsSize;i++){
        c=0;
        for(j=0;j<numsSize;j++){
            if(nums[i]==nums[j])
                c++;
        }
        if(c>1)
            break;
    }
    return nums[i];
/**    int i,j,t;
    for(i=0;i<numsSize-1;i++){
        for(j=i+1;j<numsSize;j++){
            if(nums[i]>nums[j]){
                t=nums[i];
                nums[i]=nums[j];
                nums[j]=t;
            }
        }
    }
    for(i=1;i<numsSize;i++)
        if(nums[i]==nums[i-1])
            break;
    return nums[i]; **/
}
int main(void){
	int t;
	int s[5]={1,2,3,2,4};
	t=findDuplicate(s,5);
	printf("%d\n",t);
	
} 
