#include<stdio.h>
void merge(int* nums1, int m, int* nums2, int n) {
    int i = m - 1,j = n - 1,k = m + n - 1;
    while(i >= 0 && j >= 0)
    {
        if(nums1[i] > nums2[j])
            nums1[k--] = nums1[i--];
        else
            nums1[k--] = nums2[j--];
    }
    while(j >= 0)
        nums1[k--] = nums2[j--];
}
int main(void){
	int a[6]={1,2,3,0,0,0};
	int b[3]={4,5,6};
	int t,i;
	merge(a,3,b,3);
	for(i=0;i<6;i++)
		printf("%3d",a[i]);
}
