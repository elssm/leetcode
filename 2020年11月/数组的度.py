class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b=list(set(nums)) #先对数组进行去重
        c=[]    #用于统计每个数出现的次数
        d=[]    #统计出现次数的一个或多个值
        index=[]    #每一个出现次数最多的数的所有下标
        mins=[] #用来存放出现次数最多的数的最短距离
        for i in b: #去重之后统计每个数出现的次数
            c.append(nums.count(i))
        maxnum = max(c) #表示次数最大的个数
        for i in range(len(c)): #添加出现次数最多的一个或多个数
            if maxnum == c[i]:
                d.append(b[i])
        for i in d: #外循环：对出现最多的一个或几个数进行循环
            index=[]
            for j in range(len(nums)):  #内循环：统计出现次数最多的数的所有下标
                if nums[j] == i:
                    index.append(j)
            maxindex=max(index) #出现次数最多的数的最大的下标
            minindex=min(index) #出现次数最多的数的最小的下标
            mins.append(maxindex-minindex) 
        return min(mins)+1
        # print(min(mins)+1)