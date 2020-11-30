class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=sorted(nums)
        c=[]
        for i in range(1,len(nums)):
            if a[i]==a[i-1]:
                c.append(a[i])
        b=set(a)
        b=list(b)
        for i in range(len(b)):
            if b[i]!=i+1:
                c.append(i+1)
                break;
        if len(c)==1:
            c.append(len(a))
        return c