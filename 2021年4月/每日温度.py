class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res=[0 for _ in range(len(T))]
        stack=[]
        # print(s)
        for k,v in enumerate(T):
            if stack:
                while stack and T[stack[-1]] < v:
                    res[stack[-1]] = k - stack[-1]
                    stack.pop()
            stack.append(k)
        return res
