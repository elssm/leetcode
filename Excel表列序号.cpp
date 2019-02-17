#include<stdio.h>
#include<string.h>
int titleToNumber(char* s) {
    int t,i;
    int sum=0;
    t=strlen(s);
    for(i=0;i<t;i++){
    	sum=sum*26+(s[i]-64);
    }
    printf("%d\n",sum);
}
int main(void){
	char s[10]="BB";
	titleToNumber(s);
} 


