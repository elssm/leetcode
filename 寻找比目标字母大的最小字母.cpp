#include<stdio.h>
char nextGreatestLetter(char* letters, int lettersSize, char target) {
    int i,j;
    char *t;
    for(i=0;i<lettersSize-1;i++){
    	for(j=i+1;j<lettersSize;j++){
    		if(letters[i]>letters[j]){
    			*t=letters[i];
    			letters[i]=letters[j];
    			letters[j]=*t;
    		}
    	}
    }
    for(i=0;i<lettersSize;i++){
    	if(letters[i]>target)
    		break;
    }
    if(i==lettersSize)
    	putchar(letters[0]);
    else
    	putchar(letters[i]);
}
int main(void){
	char s[10]="cjf";
	nextGreatestLetter(s,3,'z');
} 
