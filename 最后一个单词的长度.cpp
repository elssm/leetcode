#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int lengthOfLastWord(char* s) {
    int len=strlen(s);
    int i;
    int count=0;
    while(s[len-1]==32){   //�ж����һ���ǲ��ǿո� ����Ǿ��������ȴӶ�ɾ���ո� 
    	len--;
    }
    for(i=len-1;s[i]!=32&&i>=0;i--)
    	count++;
    	
    return count;
}
int main(void){
	char s[100]="asd";
	int t;
	t=lengthOfLastWord(s);
	printf("%d\n",t);
} 

