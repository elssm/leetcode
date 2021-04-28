class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def trace(path,result,index):
            if result < 0:
                return
            if result == 0:
                res.append(path)
                return 
            for i in range(index,len(candidates)):
                if result >= candidates[i]:
                    trace(path+[candidates[i]],result-candidates[i],i)
                else:
                    break
        res = []
        candidates.sort()
        trace([],target,0)
        return res