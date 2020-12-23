class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        s = ""
        if len(nums)==0:
            return []
        if len(nums)==1:
            s = str(nums[0])
            res.append(s)
            return res
        start = str(nums[0])
        end = str(nums[0])
        nums.append(0) #给列表添加一个0为了遍历到最后一个元素
        i=1
        while i<len(nums):
            if nums[i]-nums[i-1]!=1:
                if start == end:
                    s = start
                else:
                    s = start + "->" + end
                res.append(s)
                start = str(nums[i])
                end = str(nums[i])
                i+=1
            else:
                end = str(nums[i])
                i+=1
        return res
