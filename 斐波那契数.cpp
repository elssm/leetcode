#include<stdio.h>
int fib(int N) {
    if(N<=1)
		return N;
	else
		return fib(N-1)+fib(N-2);
}
int main(void){
	int t=10;
	int s=fib(t);
	printf("%d\n",s);
} 
