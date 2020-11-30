#include <stdio.h>
#include "stdlib.h"
int* findDuplicates(int* nums, int numsSize){
    int i,count=0;
    int b=0;
    for(i=0;i<numsSize;i++){
        if(nums[abs(nums[i])-1]>0){
            nums[abs(nums[i])-1]=-abs(nums[abs(nums[i])-1]);
        }else{
            nums[abs(nums[i])-1]=numsSize+1;
        }
    }
//    for(i=0;i<numsSize;i++){
//        printf("%5d",nums[i]);
//    }
//    printf("\n");
    for(i=0;i<numsSize;i++){
        if(nums[i]==numsSize+1)
            count++;
    }
    int *ret=(int *)malloc(sizeof(int)*count);
    for(i=0;i<numsSize;i++){
        if(nums[i]==numsSize+1)
            ret[b++]=i+1;
    }
    for(i=0;i<b;i++){
        printf("%d\n",ret[i]);
    }
//    return ret;
}
int main(){
    int a[8]= {4,3,2,7,8,2,3,1};
    findDuplicates(a,8);
}