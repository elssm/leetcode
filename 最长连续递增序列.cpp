#include<stdio.h>
int findLengthOfLCIS(int* nums, int numsSize) {
    int i,j,temp=0;
    int t=1;
    if(numsSize==0)
        return 0;
    else{
        for(i=1;i<numsSize;i++){
    	if(nums[i]>nums[i-1])
			t++;
		else{
			if(t>temp)
				temp=t;
			t=1;
		} 
    }
    return t>temp?t:temp;
    }
}
int main(void){
	int s[5]={1,3,5,4,7};
	int t;
	t=findLengthOfLCIS(s,5);
	printf("%d\n",t);
} 
