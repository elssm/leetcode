//已知一个奇怪的队列，这个队列中有n个数，初始状态时，顺序
//是1，2，3，4...n,这个队列只支持一种操作，就是把队列中的第
//i号元素提前到队首，如有四个元素，初始为1，2，3，4 可以将
//3提前到队首，得到3，1，2，4
//现在给出几个经过若干次操作之后的序列，请你找出这个序列至少是
//由原序列操作了多少次得到的。 
#include<stdio.h>
int main(){
	int n,i,j,count=0;
	int a[1000];
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	for(i=n-2;i>=0;i--){
		if(a[i]>a[i+1])
			break;
	}
	if(i<0)
		printf("%d",count);
	else
		printf("%d",i+1);
	return 0;
	
} 
