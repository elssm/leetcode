class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        c=[]
        for i in range(len(ops)):
            if ops[i]=='C':
                c.pop(-1)
            elif ops[i]=='D':
                c.append(c[-1]*2)
            elif ops[i]=='+':
                c.append(c[-1]+c[-2])
            else: #如果不是CD+，则一定是数字，直接append
                c.append(int(ops[i]))
        return sum(c)