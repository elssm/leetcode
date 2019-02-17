#include<stdio.h>
bool isPowerOfFour(int num) {
	int count=0;
    if(num==1)
    	printf("true");
    else{
    	if(num<4)
    		printf("false");
    	else{
    		while(num>4){
    			count=count+(num%4);
    			num/=4;
    			
    		}
    		if(num==4&&count==0)  //每次取余4为0，所以count一直相加为0 
    			printf("true");
    		else
    			printf("false");
    	}
    }
}
int main(void){
	int t=17;
	isPowerOfFour(t);
} 
