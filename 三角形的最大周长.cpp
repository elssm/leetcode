#include<stdio.h>
/**int largestPerimeter(int* A, int ASize) {    //此方法超时 
    int sum=0;
    int i,j,k;
    if(ASize<3)
        return sum;
    else
        for(i=0;i<ASize-2;i++){
            for(j=i+1;j<ASize-1;j++){
                for(k=j+1;k<ASize;k++){
                	//printf("%3d%3d%3d\n",A[i],A[j],A[k]);
                    if(A[i]+A[j]>A[k]&&A[i]+A[k]>A[j]&&A[j]+A[k]>A[i]){
                        if(A[i]+A[j]+A[k]>sum)
                            sum=A[i]+A[j]+A[k];
                        else
                            continue;
                    }
                }
            }
        }
    printf("%d\n",sum);//return sum;
} **/

/**void quicksort(int s[],int low,int high)
{
    if(low<high)
    {
        int i=low,j=high,x=s[low];
        while(i<j)
        {
            while(i<j && s[j]>=x) // 从右向左找第一个小于x的数
				j--;  
            if(i<j) 
				s[i++]=s[j];
			
            while(i<j && s[i]<x) // 从左向右找第一个大于等于x的数
				i++;  
            if(i<j) 
				s[j--]=s[i];
        }
        s[i] = x;
        quicksort(s,low,i-1); // 递归调用 
        quicksort(s,i+1,high);
    }
}
int largestPerimeter(int* A, int ASize) {
    int sum=0;
    int i,j,k;
    quicksort(A,0,ASize);
    for(i = ASize - 1; i >= 2; i--)  
    {
        if(A[i] < (A[i-1] + A[i-2])){
            sum = A[i] + A[i-1] + A[i-2];
            return sum; //printf("%d\n",sum);//return sum;
        }
}
    return 0;
} **/


int largestPerimeter(int* A, int ASize) {
    
    int i,j,t,cp=0,sum=0;
	for(i=ASize-1;i>0;i--)
	{
	for(j=0;j<i;j++)
	if(A[j]>A[j+1])
	{
		t=A[j];
		A[j]=A[j+1];
		A[j+1]=t;
		cp=1;
	}
	if(!(cp))
	break;
	}
    

    //quicksort(A,0,ASize);
    for(i = ASize - 1; i >= 2; i--)  
    {
        if(A[i] < (A[i-1] + A[i-2])){
            sum = A[i] + A[i-1] + A[i-2];
            return sum; //printf("%d\n",sum);//return sum;
        }
}
    return 0;
}

int main(void){
	int t[4]={1,2,3,4};
	int s;
	s=largestPerimeter(t,4);
	printf("%d\n",s);
} 
