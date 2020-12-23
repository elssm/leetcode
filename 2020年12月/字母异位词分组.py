class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #方法一
        res=[]
        c=[]
        result=[]
        for i in range(len(strs)):
            res.append((strs[i],Counter(strs[i])))
        while len(res)!=0:
            temp=res[0][1]
            num=[]
            count=[]
            for i in range(len(res)):
                if temp==res[i][1]:
                    num.append(res[i][0])
                    count.append(i)
            result.append(num)
            for i in reversed(count):
                res.pop(i)
        return result

        #其他解法
        # res = []
        # dic = {}
        # for s in strs:
        #     keys = "".join(sorted(s))
        #     if keys not in dic:
        #         dic[keys] = [s]
        #     else:
        #         dic[keys].append(s)
        # return list(dic.values())