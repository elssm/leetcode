#include<Stdio.h>
#include<string.h>
#include<stdlib.h>
bool canConstruct(char* ransomNote, char* magazine) {
    int i, x[26] = { 0 }, y[26] = { 0 };
	for (i = 0; ransomNote[i] != '\0'; i++)	x[ransomNote[i] - 'a']++;	//建立 ransomNote 的字符表 x
	for (i = 0; magazine[i] != '\0'; i++)	y[magazine[i] - 'a']++;	   //建立 magazine 的字符表 y
	for (i = 0; i < 26; i++)							              //比较两字符表是否相同
		if (x[i] > y[i])	
			printf("false");//return false;
	printf("true");//return true;
}
int main(void){
	char s[10]="anbgram";
	char t[10]="nagaram";
	canConstruct(s,t);
	
} 
