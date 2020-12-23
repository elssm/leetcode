class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        c1=0
        d1={}
        res1=[]
        c2=0
        d2={}
        res2=[]
        for i in pattern:
            if i in d1.keys():
                res1.append(d1[i])
            else:
                d1[i]=c1
                res1.append(c1)
                c1+=1
        for i in s.split(" "):
            if i in d2.keys():
                res2.append(d2[i])
            else:
                d2[i]=c2
                res2.append(c2)
                c2+=1
        return res1==res2