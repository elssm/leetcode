class Solution(object):
    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
        c = 0
        for i in range(3):
            if guess[i] == answer[i]:
                c+=1
        return c 