#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int* selfDividingNumbers(int left, int right, int* returnSize) {
    int i,j,temp,temp1,t;
    int *ret = (int *)malloc(sizeof(int) * 1000); //分配空间 
    *returnSize=0;
    for(i=left;i<=right;i++){
    	temp=temp1=i;
        while(temp){
        	if(temp%10==0)  //如果数字中有零出现则跳出while循环 
        		break;
        	else{
        		t=temp%10;  //否则就继续判断每一位 
            if(temp1%t==0)
                temp/=10;
            else
                break;
        }
        if(temp!=0)
            continue;
        else
            ret[(*returnSize)++]=temp1;
            //printf("%3d",temp1);
        	}
    }
    for(i=0;i<*returnSize;i++){
    	printf("%5d",ret[i]);
    }
    //return ret;
}
int main(void){
	int returnSize;
	selfDividingNumbers(78,120,&returnSize);
} 






