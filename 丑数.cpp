#include<stdio.h>
bool isUgly(int num) {
    if(num<6&&num>0)
        return true;
    if(num<1)
        return false;
    else{
        while(num>1){
            if(num%2==0)
                num/=2;
            else if(num%3==0)
                num/=3;
                else if(num%5==0)
                    num/=5;
                    else
                        return false;
        }
        return true;
    }
} 
