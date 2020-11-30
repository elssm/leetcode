class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        for i in range(len(digits)):
            if digits[i]<9:
                digits[i]+=1
                digits.reverse()
                return digits
            else:
                if i+1==len(digits):
                    digits[i]=0
                    digits.append(1)
                    digits.reverse()
                    return digits
                else:
                    digits[i]=0