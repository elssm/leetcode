#include<stdio.h>
int singleNumber(int* nums, int numsSize) {
    int i,j;
    int a;
    int count=0;
    for(i=0;i<numsSize;i++){
    	count=0;
        a=nums[i];
        for(j=0;j<numsSize;j++){
            if(a==nums[j])
                count++;
        }
        if(count==1)
            printf("%d\n",a);//return a;
        else
            continue;
    }
    //return a;
}  

/**int singleNumber(int* nums, int numsSize) {  //利用异或，学到了！ 
    int t=0;
	int i;
	for(i=0;i<numsSize;i++){
		t=t^nums[i];
	} 
	printf("%d\n",t);//return t;
} **/ 
int main(void){
	int a[3]={1,0,1};
	singleNumber(a,3);
} 
