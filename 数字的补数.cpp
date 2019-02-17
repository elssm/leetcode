#include<stdio.h>
int findComplement(int num) {
    int i,t,count=0;
	int a[100];
	int sum=0;
	while(num){
		t=num%2;
		a[count++]=t;
		num=num/2;
	}
	for(i=count-1;i>=0;i--){
		t=1^a[i];   //È¡·´ 
		sum=sum*2+t;
	}
    return sum;
}
int main(void){
	int t=10;
	int s;
	s=findComplement(t);
	printf("%d\n",s); 
} 



