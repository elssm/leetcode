class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        #方法一
        result=0
        for i in range(L,R+1):
            flag=1
            count=0
            while i:
                count+=1
                i=(i-1)&i
            if count>1:
                for i in range(2,count):
                    if(count%i)==0:
                        flag=0
                if flag:
                    result+=1
        return result

        #其他大佬的答案
        # temp = [2, 3, 5, 7, 11, 13, 17, 19]
        # return len([i for i in range(L, R + 1) if bin(i).count('1') in temp])
