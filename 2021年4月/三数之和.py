class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #第一种方法，可行但超时
        # if len(nums)==0 or len(nums)==1 or len(nums)==2:
        #     return []
        # sum_two=[]
        # d={}
        # res=[]
        # count=0
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         d[count]=[i,j]
        #         sum_two.append(nums[i]+nums[j])
        #         count+=1
        # # print(d)
        # # print(sum_two)
        # for i in range(len(nums)):
        #     for j in range(len(sum_two)):
        #         if i not in d[j] and nums[i]+sum_two[j]==0:
        #             temp = [nums[d[j][0]]] + [nums[i]] + [nums[d[j][1]]]
        #             temp.sort()
        #             if temp not in res:
        #                 res.append(temp)
        # # res = list(set([tuple(t) for t in res]))
        # # res = list([list(l) for l in res])
        # return res

        #第二种方法，还是超时....
        # d = {}
        # res = []
        # count=0
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         d[count] = [i,j]
        #         count+=1
        # for k in range(len(nums)):
        #     for v in d.values():
        #         if k not in v and nums[v[0]]+nums[v[1]]+nums[k]==0:
        #             temp = [nums[v[0]],nums[v[1]],nums[k]]
        #             temp.sort()
        #             if temp not in res:
        #                 res.append(temp)
        # return res

        #参考别人的方法
        d = {}
        res = []
        for i in range(len(nums)):
            d = {}
            for j in range(i + 1, len(nums)):
                key = nums[j]
                if key in d:
                    value = d[key] + [key]
                    value.sort()
                    if value not in res:
                        res.append(value)
                key = -nums[i] - nums[j]
                if key not in d:
                    d[key] = [nums[i], nums[j]]
        return res