#include<stdio.h>
#include<stdlib.h>
#include<string.h> 
bool containsDuplicate(int* nums, int numsSize) {
    int i,j,count=1;  
    if(numsSize<1)
        printf("false");//return false;
    else{
        for(i=1;i<numsSize;i++){
        for(j=0;j<i;j++){
            if(nums[i]==nums[j]){
                break;
            }
        }
            if(j==i)
                count++;
            else
                ;
    }
    if(count==numsSize)
        printf("false");//return false;
    else
        printf("true");//return true;
    }
}
int main(void){
	int t[0]={};
	containsDuplicate(t,0);
}
