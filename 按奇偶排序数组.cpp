#include<stdio.h>
#include<string.h>
#include<stdlib.h>
/**int* sortArrayByParity(int* A, int ASize) {
    int i,j;
    int temp;
    for(i=1;i<ASize;i++){
        if(A[i]%2==0){
            temp=A[i];
            for(j=i;j>0;j--)
                A[j]=A[j-1];
            A[j]=temp;
        }
    }
    for(i=0;i<ASize;i++)
    printf("%3d",A[i]);
}
int main(void){
	int t[5]={1,3,2,4,5}; 
	int i;
	sortArrayByParity(t,5);	
}**/ 
int* sortArrayByParity(int* A, int ASize, int* returnSize) {
    *returnSize=ASize;//不太清楚什么意思
    int i,j;
    int temp;
    for(i=1;i<ASize;i++){
        if(A[i]%2==0){
            temp=A[i];
            for(j=i;j>0;j--)
                A[j]=A[j-1];
            A[j]=temp;
        }
    }
    return A;
}
