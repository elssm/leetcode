#include<stdio.h>
#include<stdlib.h>
#include<string.h>
bool isPalindrome(char* s) {
    int len=strlen(s);
    int i;
    int a[len+1]; //此处加一是因为如果输入是空字符的话，则len=0，此时系统会返回 
    int b[len+1]; //variable length array bound evaluates to non-positive value 0错误 
    int t=0;
    int flag=0;
    int count=0;
    for(i=0;i<len;i++){
        if((s[i]>=97&&s[i]<=122)||(s[i]>=48&&s[i]<=57))
            a[count++]=s[i];
        else
            if(s[i]>=65&&s[i]<=90)
                a[count++]=s[i]+32;
            else
                continue;
    }
    for(i=count-1;i>=0;i--)
        b[t++]=a[i];
    for(i=0;i<count;i++)
    	if(a[i]==b[i])
    		flag++;
    if(flag==count)
    	printf("true");
    else
    	printf("false");
}
int main(void){
	char s[100]=" ";//"A man, a plan, a canal: Panama";
	isPalindrome(s);
	
}  

/**int main(void){
	char s[5]="a, a";
	if((s[1]>=97&&s[1]<=122)||(s[1]>=48&&s[1]<=57))
	printf("y");
	else
	printf("n");
}**/
