class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.getways(n, {})

    def getways(self, n, memo={}):
        if n in memo:
            return memo[n]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            ways = self.getways(n-1) + self.getways(n-2)   
            memo[n] = ways
            return ways

class Solution1:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        one_before = 1
        two_before = 1
        total = 0

        for i in range(n-1):
            total = one_before + two_before
            two_before = one_before
            one_before = total

        return total

class DynamicSolution:
    def climbStairs(self, n: int) -> int:
        #edge case
        if n <=0 : return 0
        if n<=2: return 2
        dp = [0]*(n+1) # considering zero steps we need n+1 places
        dp[1]= 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] +dp[i-2]
        print(dp)
        return dp[n]
s = DynamicSolution()
way = s.climbStairs(45)
print(way)