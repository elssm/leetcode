class Solution(object):
    def getKthMagicNumber(self, k):
        """
        :type k: int
        :rtype: int
        """
        print(pow(8,1.0/3))
        res = []
        for a in range(int(pow(k,1.0/2))+2):
            for b in range(int(pow(k,1.0/2))+2):
                for c in range(int(pow(k,1.0/2))+2):
                    res.append(pow(7,a)*pow(5,b)*pow(3,c))
        res = sorted(res)
        return res[k-1]