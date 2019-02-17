#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int* sortedSquares(int* A, int ASize, int* returnSize) {
    int i,j,temp;
    int *ret=(int *)malloc(sizeof(int)*((*returnSize)=ASize));
    for(i=0;i<ASize;i++){
        A[i]=A[i]*A[i];
    }
    for(i=0;i<ASize-1;i++){
        for(j=i+1;j<ASize;j++){
            if(A[i]>A[j]){
                temp=A[i];
                A[i]=A[j];
                A[j]=temp;
            }
        }
    }
    for(i=0;i<ASize;i++)
        ret[i]=A[i];
    //return ret;
    for(i=0;i<ASize;i++)
    	printf("%3d",ret[i]);
}
int main(void){
	int s[5]={-2,1,3,5,7};
	int t;
	sortedSquares(s,5,&t);
} 
