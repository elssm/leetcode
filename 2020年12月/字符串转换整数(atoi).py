class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=""
        flag=1
        temp1=["0","1","2","3","4","5","6","7","8","9"]
        temp2=["-","+"]
        temp=0
        for i in range(len(s)):
            if s[i]!=" ":
                temp=i
                break
        s=s[temp:]
        if len(s)==0 or (s[0] not in temp1 and s[0] not in temp2):
            return 0
        elif s[0] in temp1:
            for i in range(len(s)):
                if s[i] in temp1:
                    res += s[i]
                else:
                    break
            if int(res) - 2147483647 > 0:
                return 2147483647
            else:
                return int(res)
        elif s[0] in temp2:
            for i in range(1,len(s)):
                if s[i] in temp1:
                    flag=0
                    res += s[i]
                else:
                    break
            if flag:
                return 0
            elif s[0]=="-":
                if -int(res) - (-2147483648) >= 0:
                    return -int(res)
                else:
                    return -2147483648
            elif s[0]=="+":
                if int(res) - 2147483647 > 0:
                    return 2147483647
                else:
                    return int(res)
        else:
            return 0