#include<stdio.h>
bool isPalindrome(int x) {
    int k,t,sum=0;
    if(x<0)
	    return false;
	else
	{
		k=x;
		while(x!=0){
			t=x%10;
			sum=sum*10+t;
			x=x/10;
		}
		if(sum==k)
			return true;
		else
			return false;
	} 
	return 0;
}  
