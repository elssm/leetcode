#include<stdio.h>
bool isMonotonic(int* A, int ASize) {
    int i,count=0;
    if(ASize==1)
        printf("true");//return true;
    else{
    	if(A[0]<=A[ASize-1]){
        for(i=1;i<ASize-1;i++){
            if(A[i]>=A[i-1]&&A[i]<=A[i+1])
                count++;
    }
        if(count==ASize-2)
            printf("true");//return true;
        else
            printf("false");//return false;
    	}
    	else{
    	if(A[0]>=A[ASize-1]){
        for(i=1;i<ASize-1;i++){
            if(A[i]<=A[i-1]&&A[i]>=A[i+1])
                count++;
    }
        if(count==ASize-2)
            printf("true");//return true;
        else
            printf("false");//return false;
    }
    }	
    }
    return 0;
}
int main(void){
	int s[2]={1,2};
	isMonotonic(s,2);
} 
