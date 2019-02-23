#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    int i,j,k,c=0,t=1;
    int s=nums1Size>nums2Size?nums1Size:nums2Size;
    int *ret=(int *)malloc(sizeof(int)*((*returnSize)=s));
    if(nums1Size>nums2Size){
        for(i=0;i<nums2Size-1;i++){
            for(j=i+1;j<nums2Size;j++){
                if(nums2[i]>nums2[j]){
                    k=nums2[i];
                    nums2[i]=nums2[j];
                    nums2[j]=k;
                }
            }
        }
        for(i=0;i<nums2Size;i++){
            for(j=0;j<nums1Size;j++){
                if(nums2[i]==nums1[j]){
                    nums2[c++]=nums2[i];
                }
            }
        }
        ret[0]=nums2[0];
        for(i=1;i<c;i++){
            if(nums2[i]!=nums2[i-1])
                ret[t++]=nums2[i];
            else
                continue;
            
        }
        for(i=0;i<t;i++){
        	printf("%3d",ret[i]);
        }
		//return ret;
    }
    else{
        for(i=0;i<nums1Size-1;i++){
            for(j=i+1;j<nums1Size;j++){
                if(nums1[i]>nums1[j]){
                    k=nums1[i];
                    nums1[i]=nums1[j];
                    nums1[j]=k;
                }
            }
        }
        for(i=0;i<nums1Size;i++){
            for(j=0;j<nums2Size;j++){
                if(nums1[i]==nums2[j]){
                    nums1[c++]=nums1[i];
                    break;
                }
            }
        }
        ret[0]=nums1[0];
        for(i=1;i<c;i++){
            if(nums1[i]!=nums1[i-1])
                ret[t++]=nums1[i];
            else
                continue;
            
        }
        for(i=0;i<t;i++){
        	printf("%3d",ret[i]);
        }
		//return ret;
    }
}
int main(void){
	int t;
	int a[3]={4,9,5};
	int b[5]={9,4,9,8,4};
	intersection(a,3,b,5,&t);
} 
