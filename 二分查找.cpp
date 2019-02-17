#include<stdio.h>
int search(int* nums, int numsSize, int target) {
    int low=0, high=numsSize-1, mid;
    while ( low <= high ) {
        mid = (low + high) / 2;
        if(target < nums[mid]){
            high = mid - 1;
        }
        else if(target > nums[mid]){
            low = mid + 1;
        }
        else{
            return mid;
        }
    }
 
    return -1;	
}
int main(void){
	int s[6]={-1,0,3,5,9,12};
	int t;
	t=search(s,6,9);
	printf("%d\n",t);
} 
