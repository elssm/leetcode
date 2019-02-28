#include<stdio.h>
int pivotIndex(int* nums, int numsSize) {
    int i,j,k;
    int a,b;
    for(i=0;i<numsSize;i++){
        a=0;
        b=0;
        for(j=0;j<i;j++)
            a=a+nums[j];
        for(k=i+1;k<numsSize;k++)
            b=b+nums[k];
        if(a==b)
            return i;
    }
    return -1;
}
int main(void){
	int t;
	int s[5]={1,2,3,4,3};
	t=pivotIndex(s,5);
	printf("%d\n",t);
} 
