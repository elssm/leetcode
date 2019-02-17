#include<stdio.h>
#include<stdlib.h>
#include<string.h> 
bool isIsomorphic(char* s, char* t) {
    int l=strlen(s);
    int i,j,count1,count2;
    int a1[l+1],a2[l+1];   //l+1是为了防止出现空字符串 
    memset(a1,0,sizeof(a1));  //初始化a1，a2 
    memset(a2,0,sizeof(a2));
    a1[0]=a2[0]=count1=count2=1;
    for(i=1;i<l;i++){
        for(j=0;j<i;j++){
            if(s[i]==s[j]){
                a1[i]=a1[j];
                break;
            }
        }
            if(j==i){
                count1++;
                a1[i]=count1;
            }
            else
                ;
    }
    for(i=1;i<l;i++){
        for(j=0;j<i;j++){
            if(t[i]==t[j]){
                a2[i]=a2[j];
                break;
            }
        }
            if(j==i){
                count2++;
                a2[i]=count2;
            }
            else
                ;
    }
    for(i=0;i<l;i++){           //判断a1,a2数组对应值是否相等 
        if(a1[i]==a2[i])
            continue;
        else
            break;
    }
    if(i==l)
        printf("true");//return true;
    else
        printf("false");//return false;
}
int main(void){
	char s[10]="pape";
	char t[10]="fpoo";
	isIsomorphic(s,t);
} 
