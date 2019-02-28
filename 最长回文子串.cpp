#include<stdio.h>
#include<string.h>
#include<stdio.h>
char *reverse(char *s){
	int i,j,k,t,n,l;
	int count=0;
	int a=0;
	char* ret = (char*)malloc(1001);//正确定义方式 
    memset(ret,0,1001);
	//char ret[1000];这样定义在leetcode会出错 
	//char *m=(char *)malloc(sizeof(char)*strlen(s));
	t=strlen(s); 
	for(i=t;i>0;i--){
		for(j=0;j<t-i+1;j++){
			count=0;
			n=j+i-1;
			for(k=j;k<i/2+j;k++){
				if(s[k]==s[n--]){
					count++;
				}
				else
					break;
			}
			if(count==i/2)
				break;
			else
				continue;				
		}
		if(count==i/2)
			break;
		else
			continue;
}
	for(l=j;l<j+i;l++){
		ret[a++]=s[l];
		}
		return ret;
		//for(i=0;i<a;i++)
		//	putchar(ret[i]);
}
int main(){
	char s[10]="babad"; 
	reverse(s);
}
