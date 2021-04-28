class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def quicksort(i,j,res):
            if i>=j:
                return res
            p = res[i]
            low = i
            high = j
            while i<j:
                while i<j and res[j]>=p:
                    j-=1
                res[i]=res[j]
                while i<j and res[i]<=p:
                    i+=1
                res[j]=res[i]
            res[j]=p
            quicksort(low,i-1,res)
            quicksort(i+1,high,res)
            return res
        quicksort(0,len(nums)-1,nums)


        # return nums.sort()