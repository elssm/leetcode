void moveZeroes(int* nums, int numsSize){
    //思路，一遍遍历，只要遇到不是零的，直接从数组第一个数开始添加，之后把后面的数字全赋值零
    int i;
    int j=0;
    int count=0;
    for(i=0;i<numsSize;i++){
        if(nums[i]!=0){
            nums[j++]=nums[i];
            count++;
        }
    }
    for(i=count;i<numsSize;i++){
        nums[i]=0;
    }
    return nums;
}