#include<stdio.h>
#include<stdlib.h>
int longestPalindrome(char* s) {
    int i;
    int m=1;    //������Ϊ����ʱ��һ������Ҫ��һ��֮�����������Ҫ��һ
    int count=0;
    int x[58]={0};    //СдaΪ97����дAΪ65
    for(i=0;s[i]!='\0';i++){
        x[s[i] - 'A']++;       //ͳ��ÿ���ַ����ֵĸ���
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
