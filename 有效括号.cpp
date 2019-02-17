#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(void){
	int t,i,top=0;
	char s[10];
	char stack[10];
	scanf("%s",s);
	t=strlen(s);
	if(s[0]==41||s[0]==93||s[0]==125)
	printf("false");
	else{
	stack[0]=s[0];
	top++;
	for(i=1;i<t;i++){
		if(s[i]-stack[top-1]==2||s[i]-stack[top-1]==1){
			top--;
		}
		else{
			stack[top++]=s[i];
		}
	}
	if(top==0)
	printf("true");
	else
	printf("false");
}
}

