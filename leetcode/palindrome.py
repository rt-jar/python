class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        temp = x
        if x < 0:
            return False
        while x > 0:
            last_digit = x % 10
            reverse = reverse * 10 + last_digit
            x = x // 10
        return temp == reverse
        

s = Solution()
print(s.isPalindrome(121))