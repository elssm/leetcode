class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        d = {5:0,10:0,20:0}
        for i in bills:
            if i==5:
                d[5]+=1
            if i==10:
                if d[5]<1:
                    return False
                else:
                    d[5]-=1
                    d[10]+=1
            if i==20:
                if d[5]>0 and d[10]>0:
                    d[5]-=1
                    d[10]-=1
                    continue
                if d[5]>2:
                    d[5]-=3
                    continue
                else:
                    return False
        return True