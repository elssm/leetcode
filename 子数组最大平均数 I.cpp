#include<stdio.h>
double findMaxAverage(int* nums, int numsSize, int k) {
    int i,j;
    int sum;
    double t=-2147483647;
    for(i=0;i<numsSize-k+1;i++){
        sum=0;
        for(j=0;j<k;j++){
            sum=sum+nums[i+j];
            //t=sum;
        }
        if(sum>t)
            t=sum;
    }
    return t/k;
}
int main(void){
	double t;
	int s[6]={1,12,-5,-6,50,3};
	t=findMaxAverage(s,6,4);
	printf("%f",t);
} 
