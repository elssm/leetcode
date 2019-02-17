#include<stdio.h>
int repeatedNTimes(int* A, int ASize) {
    int i,j;
    int count=0;
    int a;
    for(j=0;j<ASize;j++){
    	count=0;
        a=A[j];
        for(i=0;i<ASize;i++){
        	if(A[i]==a)
        		count++;
        }
        if(count==ASize/2)
        break;
    }
     printf("%d\n",a);//return 0;    
}
int main(void){
	int t[8]={5,1,5,2,5,3,5,4};
	repeatedNTimes(t,8);
} 
