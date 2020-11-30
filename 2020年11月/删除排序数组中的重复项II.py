class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        c=0
        i=1
        j=0
        while i < len(nums):
            if nums[i]!=nums[i-1]: #如果后一个不等于前一个，和nums一样按续增加
                c += 1
                nums[c] = nums[i]
                i+=1
                count=0
            elif nums[i]==nums[i-1] and count!=1: #如果等于并且只有两个相同，按序增加
                c += 1
                nums[c]=nums[i]
                count+=1
                i+=1
            else: #这个时候是大于两个相同，后面要从i+1开始寻找，先让j=i+1
                j=i+1
                for j in range(i+1,len(nums)): #从i+1开始找，和nums[i]不相同的
                    if nums[j]!=nums[i]: #找到之后，赋值给nums[c]
                        c+=1
                        nums[c]=nums[j]
                        break #赋值结束，跳出循环
                i=j+1
                count = 0
        return c+1