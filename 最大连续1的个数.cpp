#include<stdio.h>
int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int i;
    int count=0;
    int t=0;
    for(i=0;i<numsSize;i++){
        if(nums[i]==1){
            count++;
        }
        else{
            if(count>t)
                t=count;
            count=0;
        }
    }
    /**if(count>t)
    	printf("%d\n",count);//return t;
    else
    	printf("%d\n",t);**/
    return count>t?count:t;   //三木运算符比if-else更快 
}
int main(void){
	int s[8]={0,1,0,1,1,0,0,0};
	findMaxConsecutiveOnes(s,8);
}
