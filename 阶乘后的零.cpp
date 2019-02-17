#include<stdio.h>
int trailingZeroes(int n) {
    int i,t,s=0;
	int sum=0;
	int count=5;
	t=n;
    while(t){     //判断接收的数字的范围：小于25，小于125... 
    	sum++;
    	t/=5;
    }
    for(i=0;i<sum;i++){ // n/5+n/25+n/125
    	s=s+n/count;
    	count*=5;
    }
    if(n<1808548329)  //int范围限制 
        printf("%d\n",s);//return s;
    else
        printf("%d\n",s-1);//return s-1;
}
int main(void){
	int t=138;
	trailingZeroes(t);
}

