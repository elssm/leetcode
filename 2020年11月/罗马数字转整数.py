class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans=0
        i = 1
        while i < len(s):
            if a[s[i]]>a[s[i-1]]: #如果当前大于前一个
                ans += (a[s[i]]-a[s[i-1]]) #值为ans加上当前值减去上一个值，并且i要跳两步，下一次不用在判断当前值
                i+=2
            else:
                ans+= a[s[i-1]]
                i+=1
        if a[s[len(s)-1]] <= a[s[len(s)-2]]: #额外判断最后一个字符是否小于或等于倒数第二个，是则加上最后一个
            ans+=a[s[len(s)-1]]
        return ans
