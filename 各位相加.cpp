#include<stdio.h>

/**int addDigits(int num) {       //对九取余即可，感觉这个方法很简单 
    if(num==0)
        return 0;
    int n=num%9;
    return n==0?9:n;
}**/ 

int addDigits(int num) {
    int sum=0;
    while(num>=10){
        sum=0;
        while(num){
            sum=sum+num%10;
            num/=10;
        }
        num=sum;
    }
    return num;
}
int main(void){
	int t=4323412;
	int s;
	s=addDigits(t);
	printf("%d\n",s);
} 
