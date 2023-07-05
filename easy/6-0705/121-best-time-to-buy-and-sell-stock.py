class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        n 为天数，大 K 为最多交易数
        dp[3][2][1] 的含义就是：今天是第三天，我现在手上持有着股票，至今最多进行 2 次交易 最后一个 1 是持有 | 0 是未持有
        """
        n = len(prices)
        """
        股票没了，要么头一天就没持有了，要么今天刚卖了
        dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i]);
        有股票了，要么头一天就有，要么今天刚买
        dp[i][1] = Math.max(dp[i-1][1], -prices[i]);
        """
        dp_i_0 = 0
        dp_i_1 = float('-inf')  # base case: dp[-1][0] = 0, dp[-1][1] = -infinity
        for i in range(n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        记录【今天之前买入的最小值】
        计算【今天之前最小值买入，今天卖出的获利】，也即【今天卖出的最大获利】
        比较【每天的最大获利】，取最大值即可
        """
        min_p, max_p = float("inf"), 0
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            max_p = max(max_p, prices[i] - min_p)
        return max_p


# 此方法会超时
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                ans = max(ans, prices[j] - prices[i])
        return ans


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        max_profit = 0
        for j in range(i + 1, len(prices)):
            if prices[i] < prices[j]:
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]

            elif prices[j] < prices[i]:
                i = j
        return max_profit


class Solution:
    def maxProfit(self, prices):
        min_p,max_ret = float('inf'), 0
        for one in prices:
            min_p = min(min_p, one)
            max_ret = max(max_ret, one-min_p)
        return max_ret

