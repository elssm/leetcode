class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        flag=0 #如果没有进j的循环或者没有比i更大的值，flag就会是0
        for i in nums1:
            index = nums2.index(i) #找到i在nums2中的索引
            for j in range(index+1,len(nums2)): #从索引后的第一个元素开始和i比较
                if nums2[j] > i:#如果大于i，添加到res列表中，并将flag置为1
                    res.append(nums2[j])
                    flag=1
                    break
            if flag: #如果flag为1说明存在比i大的数，并且为了下一次寻找，要将flag置为0
                flag=0
                continue
            else:
                res.append(-1)
        return res