class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        count=0
        for i in range(len(rating)-2):
            for j in range(i+1,len(rating)-1):
                for k in range(j+1,len(rating)):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        count+=1
        return count