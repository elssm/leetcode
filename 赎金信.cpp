#include<Stdio.h>
#include<string.h>
#include<stdlib.h>
bool canConstruct(char* ransomNote, char* magazine) {
    int i, x[26] = { 0 }, y[26] = { 0 };
	for (i = 0; ransomNote[i] != '\0'; i++)	x[ransomNote[i] - 'a']++;	//���� ransomNote ���ַ��� x
	for (i = 0; magazine[i] != '\0'; i++)	y[magazine[i] - 'a']++;	   //���� magazine ���ַ��� y
	for (i = 0; i < 26; i++)							              //�Ƚ����ַ����Ƿ���ͬ
		if (x[i] > y[i])	
			printf("false");//return false;
	printf("true");//return true;
}
int main(void){
	char s[10]="anbgram";
	char t[10]="nagaram";
	canConstruct(s,t);
	
} 
