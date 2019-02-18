#include<stdio.h>
int hammingDistance(int x, int y) {
    int a,b,c=0;
    if(x>y){
        while(y>0){
            a=y%2;
            b=x%2;
            if(a!=b){
                c++;
                y/=2;
                x/=2;
            }
            else{
                y/=2;
                x/=2;
            }
        }
        while(x>0){
            if(x%2==1){
                c++;
                x/=2;
            }
            else
                x/=2;
        }
        return c;
    }
    else{
        while(x>0){
            a=y%2;
            b=x%2;
            if(a!=b){
                c++;
                y/=2;
                x/=2;
            }
            else{
                y/=2;
                x/=2;
            }
        }
        while(y>0){
            if(y%2==1){
                c++;
                y/=2;
            }
            else
                y/=2;
        }
        return c;
    }
}
int main(void){
	int t;
	t=hammingDistance(1,4);
	printf("%d\n",t);
} 
