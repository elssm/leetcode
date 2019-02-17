#include<stdio.h>
int mySqrt(int x) {
    int i=1;
    while(i*i<=x&&i<46341){
        i++;
}
    if(i*i==x)
        return i;
    else
        return i-1;
    
}
int main(void){
	int t=2147483647;
	int i;
	i=mySqrt(t);
	printf("%d\n",i);
	
} 
