#include<stdio.h>
bool isHappy(int n) {
    int temp=0;
        while(n!=1)
        {
            while(n>0)
            {
                temp+=(n%10)*(n%10);
                n/=10;
            }
            n=temp;
            temp=0;
            if(n==4) 
                printf("false");//return false; 
        }
       printf("true");//return true; 
} 
int main(void){
	int t=19;
	isHappy(t);
}
