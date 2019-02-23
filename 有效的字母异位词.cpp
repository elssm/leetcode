#include<Stdio.h>
#include<string.h>
#include<stdlib.h>
bool isAnagram(char* s, char* t) {
    int i, x[26] = { 0 }, y[26] = { 0 };
	for (i = 0; s[i] != '\0'; i++)	x[s[i] - 'a']++;	//建立 s 的字符表 x
	for (i = 0; t[i] != '\0'; i++)	y[t[i] - 'a']++;	//建立 t 的字符表 y
	for (i = 0; i < 26; i++)							//比较两字符表是否相同
		if (x[i] != y[i])	
			printf("false");//return false;
	printf("true");//return true;
}
int main(void){
	char s[10]="anagram";
	char t[10]="nagaram";
	isAnagram(s,t);
} 




