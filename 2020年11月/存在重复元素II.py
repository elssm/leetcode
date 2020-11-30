class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #字典
        d={}
        for i in range(len(nums)):
            if nums[i] in d: #判断当前数字是否在字典中
                if i-d[nums[i]] <=k: #如果在，判断这个数现在的位置和字典中存的那个位置之差是否小于k
                    return True
            d[nums[i]] = i #如果不在或者大于k，则会更新这个数的位置信息
        return False