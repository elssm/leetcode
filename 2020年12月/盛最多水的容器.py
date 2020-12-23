class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #前后俩指针寻找最大高度
        i=0
        j=len(height)-1
        res=0
        while i<j:
            h=min(height[i],height[j])
            res=max(res,h*(j-i))
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return res