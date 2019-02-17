#include<stdio.h>
bool detectCapitalUse(char* word) {
    int s=strlen(word);
    int i;
    int count=0;
    if(word[0]>=65&&word[0]<=90){
        for(i=1;i<s;i++){
            if(word[i]>=65&&word[i]<=90)
                count++;
        }
        if(count==s-1||count==0)
            return true;
        else
            return false;
    }
    else{
        for(i=1;i<s;i++){
            if(word[i]>=65&&word[i]<=90)
                count++;
    }
        if(count==0)
            return true;
        else
            return false;
    
}
} 
