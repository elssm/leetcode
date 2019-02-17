#include<stdio.h>
int reverse(int x) {
      int t,sum=0;
	  while(x!=0){
	  	t=x%10;
	  	x=x/10;
        if(sum>2147483647/10||(sum==2147483647/10 && t>7))
              return 0;
        if(sum<-2147483648/10||(sum==-2147483648/10 && t<-8))
              return 0;
	     sum=sum*10+t;
      }
	  return sum;
}
int main(void)
{
	int n,sum;
	scanf("%d",&n);
	reverse(n);
	printf("%d",sum);
}

















