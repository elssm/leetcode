class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        #方法一
        count=0
        g=sorted(g)
        s=sorted(s)
        for i in g:
            for j in s:
                if j>=i:
                    s.remove(j)
                    count+=1
                    break
        return count

        #方法二
        # count=0
        # g=sorted(g)
        # s=sorted(s)
        # for i in g:
        #     j=0
        #     for j in range(len(s)):
        #         if s[j]>=i:
        #             s.remove(s[j])
        #             count+=1
        #             break