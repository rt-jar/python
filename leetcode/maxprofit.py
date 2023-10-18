class Solution(object):

    def maxProfit(self, prices):
        if not prices:
            return 0

        n = len(prices)
        # Create arrays to track the best buying and selling prices for the two transactions
        buy1 = [float('-inf')] * n
        sell1 = [0] * n
        buy2 = [float('-inf')] * n
        sell2 = [0] * n

        for i in range(n):
            # First transaction
            buy1[i] = max(buy1[i - 1], -prices[i])
            sell1[i] = max(sell1[i - 1], buy1[i - 1] + prices[i])

            # Second transaction
            buy2[i] = max(buy2[i - 1], sell1[i - 1] - prices[i])
            sell2[i] = max(sell2[i - 1], buy2[i - 1] + prices[i])

        return sell2[-1]

s = Solution()
print(s.maxProfit([7,6,5,2,4,5,1,7,8,1,9]))