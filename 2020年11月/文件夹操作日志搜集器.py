class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        count=0
        for i in range(len(logs)):
            if logs[i]=='../':
                if count>0:
                    count -=1
                else:
                    pass
            elif logs[i]=='./':
                pass
            else:
                count+=1
        return count