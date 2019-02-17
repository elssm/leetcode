#include<stdio.h>
#include<string.h>
#include<stdlib.h>
char* toLowerCase(char* str) {
    int t=strlen(str);
    int i;
    for(i=0;i<t;i++){
        if(str[i]>=65&&str[i]<=90)
            str[i]=str[i]+32;
    }
    return str;
}
int main(void){
	char a[10]="ASDfASD";
	puts(toLowerCase(a)); 
}
