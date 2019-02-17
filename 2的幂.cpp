#include<stdio.h>
bool isPowerOfTwo(int n) {
    if(n<=0)
        return false;
    else
        if((n&n-1)==0)
            printf("true");//return true;
        else
            printf("false");//return false;
}
int main(void){
	int t=256;
	isPowerOfTwo(t);
}
