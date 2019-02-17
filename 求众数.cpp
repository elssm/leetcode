#include<stdio.h>
#include<stdlib.h>
#include<string.h>
/**int majorityElement(int* nums, int numsSize) {
    int a[2][numsSize];
    memset( a, 0, sizeof(a) );
    int i,j;
    a[0][0]=nums[0];
    a[1][0]=1;
    int t=1;
    for(i=1;i<numsSize;i++){
        for(j=0;j<t;j++){
            if(nums[i]==a[0][j])
                a[1][j]++;
            else{
                a[0][t]=nums[i];
                a[1][t]+=1;
                t++;
            }
        }
    }
    for(j=0;j<t;j++){
        if(a[1][j]>numsSize/2)
            printf("%d\n",a[0][j]);
    }
    
}**/

int majorityElement(int* nums, int numsSize) {
    int a[2]={0};
    int i=0;
    int t=0;
    int j;
    while(i<numsSize){
        //a[0]=nums[i];
        a[1]=0;
        for(j=0;j<numsSize;j++){
            if(nums[j]==nums[i])
                a[1]+=1;
    }
        if(a[1]>t){
        	a[0]=nums[i];
        	t=a[1];
        }
        else
        	;
        i++;
    }
    printf("%d\n",a[0]);
}
int main(void){
	int nums[100]={6,53,53,96,45,79,53,58,53,90,40,53,53,1,53,53,89,53,33,27,53,53,84,42,53,53,87,51,66,53,28,53,53,53,50,39,36,48,19,74,38,53,42,53,99,53,80,53,53,53,53,96,78,52,24,53,53,53,53,64,10,53,53,53,53,82,53,53,53,22,53,53,67,53,53,53,53,53,67,53,19,99,53,53,21,53,69,53,53,53,52,53,96,53,53,51,81,62,4,6};
	majorityElement(nums,100);
} 
