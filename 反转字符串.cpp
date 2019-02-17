#include<stdio.h>
char* reverseString(char* s, int sSize) {
    int temp;
    int i;
    for(i=0;i<sSize/2;i++){
        temp=s[i];
        s[i]=s[sSize-i-1];
        s[sSize-i-1]=temp;
    }
    return s;
}
int main(void){
	  int i;
	  char c[10]={'c', 'a', 'p', 'r', 'o', 'g', 'r', 'a','m'};
	  reverseString(c,9);
	  for(i=0;i<9;i++){
	  	putchar(c[i]);
	  }
} 
