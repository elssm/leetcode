#include<stdio.h>
int hammingWeight(uint32_t n){
    int c = 0;
    while ( n > 1 ) {
        if( n%2 == 1 ){
            c++;
        }
        n /= 2;
    }
    if(n==1){
        printf("%d\n",c+1);
    }else{
        printf("%d\n",c);
    }
}
int main(void){
	int t=00000000000000000000000000000001;
	hammingWeight(t);
} 
