#include<stdio.h>
#include<stdlib.h>
int* addToArrayForm(int* A, int ASize, int K, int* returnSize) {
    int count=0;
    int i,m,j=0;
    int s,n=0;
    int f=0;
    s=K;
    while(K){
        K/=10;
        count++;
    }
    int *ret=(int *)malloc(sizeof(int)*((*returnSize)=ASize+count));
	for(i=ASize-1;i>=0;i--){
		j=A[i]+s%10+j/10;
        ret[f++]=j%10;
        s/=10;
		if(s==0)
			break;
	}
	if(i==0&&s==0){
		if(j/10)
			ret[f++]=j/10;
	}
	else if(i>0&&s==0){
		for(m=i-1;m>=0;m--){
			 ret[f++]=(A[m]+j/10)%10;
			 j=A[m]+j/10;
		}
		if(j/10)
			ret[f++]=j/10;
	}
		else if(i<0&&s>0){
		while(s){
			ret[f++]=s%10+j/10;
			j/=10;
			s/=10;
		}
	}
	for(i=f-1;i>=0;i--)
		printf("%d",ret[i]); 
//	int *retn=(int *)malloc(sizeof(int)*((*returnSize)=f-1));
//	for(i=f-1;i>=0;i--)
//		retn[n++]=ret[i]; 
//	for(i=0;i<n;i++)
//		printf("%d",retn[i]);
}
int main(void){
	int t;
	int a=1;
	int s[10]={9,9,9,9,9,9,9,9,9,9};
	addToArrayForm(s,10,a,&t);
} 
