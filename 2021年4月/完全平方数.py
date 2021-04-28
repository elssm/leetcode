class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        #n = (4^a)*(8b+7) return 4
        while n%4==0:
            n/=4
        if n%8==7:
            return 4
        a=0
        #n=a**2 + b**2 return 1 or 2
        while a**2 <=n:
            b= int((n-a**2)**0.5)
            if a**2 + b**2 == n: 
                if a>0:
                    a=1
                if b>0:
                    b=1
                return a+b
            a+=1
        return 3