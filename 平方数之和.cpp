#include<stdio.h>
#include<math.h>
bool judgeSquareSum(int c) {
    int i=0,j=sqrt(c),num;
    if(sqrt(c)>46340)
        return false;
    if(c<2)
        return true;
    else{
        while(i<=j){
                num=i*i+j*j;
                if(num==c)
                    return true;
                else if(num<c)
                    i++;
                else
                    j--;
    		}		
}
        return false;
     
    }

int main(void){
	judgeSquareSum(5);
} 
