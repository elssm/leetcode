#include<stdio.h>
#include<stdlib.h>
int longestPalindrome(char* s) {
    int i;
    int m=1;    //当个数为奇数时第一个数需要加一，之后的数都不需要加一
    int count=0;
    int x[58]={0};    //小写a为97，大写A为65
    for(i=0;s[i]!='\0';i++){
        x[s[i] - 'A']++;       //统计每个字符出现的个数
    }
    for(i=0;i<58;i++){
        if(x[i]>1&&x[i]%2==0)
            count+=x[i];
        if(x[i]%2==1){
            count+=x[i]-1+m;
            m=0;
        }
    }
    return count;
} 
int main(void){
	int t;
	char s[10]="abccccdd";
	t=longestPalindrome(s);
	printf("%d\n",t);
}
