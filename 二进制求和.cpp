#include<stdio.h>
#include<string.h>
#include<stdlib.h>
char* addBinary(char* a, char* b) {
    int al=strlen(a);
    int bl=strlen(b);
    int len=al>bl?al+2:bl+2;
    char *result=(char*)malloc(len+1);
    int i,j,cur,temp;
    i=al-1,j=bl-1;
    temp=cur=0;
    while(i>=0&&j>=0){
       if((a[i]-'0')+(b[j]-'0')==2){
           if(temp==1){
               result[cur]='1';  //ÊäÈë: a = "1010", b = "1011" Êä³ö: "10101"
           }else{
               result[cur]='0';
           }
           temp=1;
       }else if((a[i]-'0')+(b[j]-'0')==1){
           if(temp==1){
             result[cur]='0';
             temp=1;
           }else{
              result[cur]='1';
              temp=0;
           }
       }else{
           result[cur]=temp+'0';
           temp=0;
       }
       --i,--j,++cur;
    }
    while(i>=0){
        if(temp==1&&a[i]=='0'){
            result[cur]='1';
            temp=0;
        }else if(temp==1&&a[i]=='1'){
            result[cur]='0';
            temp=1;
        }else{
            result[cur]=a[i];
        }
        ++cur,--i;
    }
     while(j>=0){
        if(temp==1&&b[j]=='0'){
            result[cur]='1';
            temp=0;
        }else if(temp==1&&b[j]=='1'){
            result[cur]='0';
            temp=1;
        }else{
            result[cur]=b[j];
        }
        ++cur,--j;
    }
    if(temp==1)
      result[cur++]='1';
    result[cur]='\0';
    int t=0;
    for(int k=0,m=cur-1;k<m;++k,--m){
        t=result[k];
        result[k]=result[m];
        result[m]=t;
    }
    return result;
} 
int main(void){
	int i;
	char *s;
	char a[10]="101010";
	char b[10]="100";
	s=addBinary(a,b);
	puts(s);
	
}



