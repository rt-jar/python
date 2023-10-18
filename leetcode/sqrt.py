class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        guess = 1
        while True:
            newGuess = 0.5 * (guess + x/guess)
            if abs(newGuess - guess) < 0.01:
                return int(newGuess)
            guess = newGuess

s = Solution()
print(s.mySqrt(1234)) 