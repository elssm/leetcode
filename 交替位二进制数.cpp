#include<stdio.h>
bool hasAlternatingBits(int n) {
    int m;
    int t=n%2;
    n=n/2;
    while(n){
        m=n%2;
        if(m!=t){
            n/=2;
            t=m;
        }
        else
            break;
    }
    if(n==0)
        printf("true");//return true;
    else
        printf("false");//return false;
}
int main(void){
	hasAlternatingBits(5);
} 
