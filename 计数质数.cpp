#include<stdio.h>
int countPrimes(int n) {
    int i,j;
    int count=0;
    if(n<3)
    	return count;
    else{
    	for(i=n-1;i>2;i--){
        for(j=2;j<i;j++){
            if(i%j==0)
            break;
            }
            if(j==i)
                count++;
         }
    return count+1;
    }
}
int main(void){
	int t=100;
	int s;
	s=countPrimes(t);
	printf("%d\n",s); 
} 
