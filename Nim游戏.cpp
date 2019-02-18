#include<stdio.h>
bool canWinNim(int n) {     //给对手留下4的倍数的石头就能赢
    if(n%4!=0)
        return true;
    else
        return false;
} 
