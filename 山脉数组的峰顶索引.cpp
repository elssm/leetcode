#include<stdio.h>
int peakIndexInMountainArray(int* A, int ASize) {
    int i;
    for(i=1;i<ASize-1;i++){
        if(A[i]>A[i-1]&&A[i]>A[i+1])
            break;
    }
    return i;
}
int main(void){
	int t;
	int s[5]={1,2,3,1,0};
	t=peakIndexInMountainArray(s,5);
	printf("%d\n",t);
} 
