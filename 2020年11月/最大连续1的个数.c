int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int i;
    int count=0;
    int t=0;
    for(i=0;i<numsSize;i++){
        if(nums[i]==1){
            count++;
        }
        else{
            if(count>t)
                t=count;
            count=0;
        }
    }
    return count>t?count:t;
}