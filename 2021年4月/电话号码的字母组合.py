class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res=[]
        d={2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}
        if len(digits)==0:
            return []
        if len(digits)==1:
            return d[int(digits)]
        l = len(digits)
        if l==2:
            for i in d[int(digits[0])]:
                for j in d[int(digits[1])]:
                    res.append(i+j)
        if l==3:
            for i in d[int(digits[0])]:
                for j in d[int(digits[1])]:
                    for k in d[int(digits[2])]:
                        res.append(i+j+k)
        if l==4:
            for i in d[int(digits[0])]:
                for j in d[int(digits[1])]:
                    for k in d[int(digits[2])]:
                        for m in d[int(digits[3])]:
                            res.append(i+j+k+m)
        return res