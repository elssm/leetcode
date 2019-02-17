#include<stdio.h>
bool isPowerOfThree(int n) {
    int count=0;
    if(n==1)
    	printf("true");
    else{
    	if(n<3)
    		printf("false");
    	else{
    		while(n>3){
    			count=count+(n%3);
    			n/=3;
    			
    		}
    		if(n==3&&count==0)  
    			printf("true");
    		else
    			printf("false");
    	}
    }
}
int main(void){
	int t=27;
	isPowerOfThree(t);
} 
