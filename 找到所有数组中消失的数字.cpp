#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize) {
    int i,count=0;
    int b=0;
    for(i=0;i<numsSize;i++){
        nums[abs(nums[i])-1]=-abs(nums[abs(nums[i])-1]);//别人的方法 
    }													//没看懂 
    for(i=0;i<numsSize;i++){
        if(nums[i]>0)
            count++;
    }
    int *ret=(int *)malloc(sizeof(int)*((*returnSize)=count));
    for(i=0;i<numsSize;i++){
        if(nums[i]>0)
            ret[b++]=i+1;
    }
    for(i=0;i<b;i++)
    	printf("%3d",ret[i]);
    //return ret;
}
/**int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize) {
    int i,j,t,a=0;
    int b=0;                   //我的方法...超时了...... 
    int c=1;
    if(numsSize==0)
        return nums;
    else{
        // int *ret=(int *)malloc(sizeof(int)*((*returnSize)=2));
    for(i=0;i<numsSize-1;i++){
        for(j=i+1;j<numsSize;j++){
            if(nums[i]>nums[j]){
                t=nums[i];
                nums[i]=nums[j];
                nums[j]=t;
            }
        }
    }
    nums[a]=nums[0];
    for(i=1;i<numsSize;i++){
        if(nums[i]!=nums[a])
            nums[++a]=nums[i];
    }
    int *ret=(int *)malloc(sizeof(int)*((*returnSize)=numsSize-a-1));
    for(i=1;i<numsSize+1;i++){
        for(j=0;j<a+1;j++){
            if(nums[j]==i)
                break;
        }
        if(j<a+1)
            continue;
        else
            ret[b++]=i;
    }
    //for(i=0;i<a+1;i++){
      //  if(nums[i]!=c++){	 
        //    ret[b++]=c-1;
          //  i--; 
        //}
    //}
	return ret;
    }
}   **/
int main(void){
	int s[2]={1,1};
	int t;
	findDisappearedNumbers(s,2,&t);
} 
