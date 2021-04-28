class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0
        
        #两层循环时间复杂度太大了。不过思路没问题
        # ans=0
        # start=0
        # end=0
        # max_h = max(height)
        # for i in range(1,max_h+1):
        #     for j in range(len(height)):
        #         if height[j]>=i:
        #             start=j
        #             break
        #     for k in range(len(height)):
        #         if height[len(height)-k-1]>=i:
        #             end=len(height)-k-1
        #             break
        #     for j in range(start+1,end):
        #         if height[j]<i:
        #             ans+=1
        # return ans

        #找到最大值
        max_h = max(height)
        #找到最大值的下标(第一个最大值)
        index = height.index(max_h)
        ans=0
        temp=0
        #从左到最大值遍历
        for i in range(index):
            if height[i]<height[temp]:
                ans=ans+(height[temp]-height[i])
            else:
                temp=i
        height=list(reversed(height[index:]))
        temp2=0
        for i in range(len(height)):
            if height[i]<height[temp2]:
                ans=ans+(height[temp2]-height[i])
            else:
                temp2=i
        return ans