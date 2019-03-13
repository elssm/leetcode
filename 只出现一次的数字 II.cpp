#include<stdio.h>
int singleNumber(int* nums, int numsSize) {
    int i,j,c;
    for(i=0;i<numsSize;i++){
        c=0;
        for(j=0;j<numsSize;j++){
            if(nums[j]==nums[i])
                c++;
        }
        if(c==1)
            break;
    }
    return nums[i];
}
int main(void){
	int t;
	int s[4]={1,3,1,1};
	t=singleNumber(s,4);
	printf("%d\n",t);
	
} 
