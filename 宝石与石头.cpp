#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int numJewelsInStones(char* J, char* S) {
    int count=0;
    int m,n;
    int i=strlen(J);
    int j=strlen(S);
    for(m=0;m<i;m++){
        for(n=0;n<j;n++){
            if(J[m]==S[n])
                count++;
            else
                continue;
        }
    }
    return count;
} 
int main(void){
	char a[10]="aA";
	char b[10]="aaAAAbbb";
	int t;
	t=numJewelsInStones(a,b);
	printf("%d\n",t);
}
