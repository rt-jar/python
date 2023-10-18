class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
    
        carry = 1
        

        for i in range(len(digits)-1, -1, -1):
            digits[i] = digits[i] + carry
            if digits[i] > 9:
                digits[i] = 0
                carry = 1
            else:
                carry = 0
                return digits
            if i == 0 and carry == 1:
                return [1] + digits
    
        return digits


s = Solution()
print(s.plusOne([9,9,9,9,9]))
print(s.plusOne([8,9,9,9,9]))