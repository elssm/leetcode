#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int* sortArrayByParityII(int* A, int ASize, int* returnSize) {
    int i,temp,a=0,b=ASize-1;
    int *ret=(int *)malloc(sizeof(int)*((*returnSize)=ASize));
    for(i=0;i<ASize;i++){
        if(A[i]%2==0){
            ret[a++]=A[i];
        }
        else
            ret[b--]=A[i];
    }
   // for(i=0;i<ASize;i++)
    //	printf("%3d",ret[i]);
    for(i=1;i<ASize/2;i+=2){
        temp=ret[i];
        ret[i]=ret[ASize-i-1];
        ret[ASize-i-1]=temp;
    }
    for(i=0;i<ASize;i++)
    	printf("%3d",ret[i]);
    //return ret;    
}
int main(void){
	int s[6]={1,2,3,4,5,6};
	int t;
	sortArrayByParityII(s,6,&t);
} 
