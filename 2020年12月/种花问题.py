class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i=0
        while i < len(flowerbed)-1:
            #如果当前值为0，则判断下一个值是否为1，如果为1，则跳到下一个为1的值开始判断
            if flowerbed[i]==0:
                if flowerbed[i+1]==1:
                    i+=1
                    continue
                #在当前值为0的情况下，如果下一个值不是1，则当前值就可以改为1，并跳到下下一个值开始判断
                if flowerbed[i+1]!=1:
                    flowerbed[i]=1
                    i+=2
                    n-=1
                    continue
            #如果当前值为1，则直接跳到下下一个值开始判断
            if flowerbed[i]==1:
                i+=2
                continue

        #i不等于0说明值大于等二2
        if i!=0:
            if flowerbed[-1]==0 and flowerbed[-2]==0:
                n-=1
        #i等于0说明只有一个值
        if i==0:
            #判断这个值是否为0
            if flowerbed[0]==0:
                n-=1
        #如果n的值小于等于0则说明插完了
        if n<=0:
            return True
        else:
            return False