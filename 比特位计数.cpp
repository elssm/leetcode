#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int* countBits(int num, int* returnSize) {
    int *ret=(int *)malloc(sizeof(int)*((*returnSize)=num+1));
    ret[0]=0;
    int count=0;
    int i;
    /**for(i=1;i<=num;i++){      //第一种方法 耗时太长 
        count=0;
        while(i){
            if(i%2==1){
                count++;
                i/=2;
            }
            i/=2;
        }
        ret[i]=count;
    }**/
    for(i=1;i<=num;i++){
      /**  if(i%2==0){			//第二种 
            ret[i]=ret[i/2];
        }
        else{
            ret[i]=ret[i/2]+1;
        }**/
        ret[i]=ret[i&(i-1)]+1;    //第三种 
    }
    //return ret;
    for(i=0;i<num;i++){
    	printf("%3d",ret[i]);
    }
}
int main(void){
	int t;
	countBits(5,&t);
} 
