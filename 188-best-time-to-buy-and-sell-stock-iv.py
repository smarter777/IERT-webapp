class Solution:
    """
    标准的三维DP动态规划，三个维度，第一维表示天，第二维表示交易了几次，第三维表示是否持有股票。

    首先初始化三维数组，填充第1天操作j次的没买或买了的情况的初始值，没买就是0，第一天就买入即-prices[0]。这里定义卖出操作时交易次数加1

    然后是状态转移方程，下面描述的i, j都大于0

    「第i天交易次数0不持有股票」的情况只能来自「第i-1天交易次数0不持有股票」；

    「第i天交易j次不持有股票」的状态可以来自「第i-1天交易j次不持有股票」或者「第i-1天交易j-1次持有股票」(即今天卖出股票，然后交易次数+1)；

    「第i天交易j次持有股票」的状态可以来自「第i-1天交易j次持有股票」或者「第i-1天交易j次不持有股票」(即今天买入股票，因为是买入操作所以交易次数不变)

    最后对于这题LeetCode的测试样例里有超大k值的情况，退化成122题不限次数的操作，可以用贪心解决或者直接替换k值为数组长度的一半
    """

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or not k:
            return 0
        n = len(prices)

        # 当k大于数组长度的一半时，等同于不限次数交易即122题，用贪心算法解决，否则LeetCode会超时，也可以直接把超大的k替换为数组的一半，就不用写额外的贪心算法函数
        if k > n // 2:
            return self.greedy(prices)

        dp, res = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)], []
        # dp[i][k][0]表示第i天已交易k次时不持有股票 dp[i][k][1]表示第i天已交易k次时持有股票
        # 设定在卖出时加1次交易次数
        for i in range(k + 1):
            dp[0][i][0], dp[0][i][1] = 0, - prices[0]
        for i in range(1, n):
            for j in range(k + 1):
                if not j:
                    dp[i][j][0] = dp[i - 1][j][0]
                else:
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] - prices[i])
        # 「所有交易次数最后一天不持有股票」的集合的最大值即为问题的解
        for m in range(k + 1):
            res.append(dp[n - 1][m][0])
        return max(res)

    # 处理k过大导致超时的问题，用贪心解决
    def greedy(self, prices):
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        作者：LeetCode-Solution
        链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-iv-by-8xtkp/
        """
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        buy = [[0] * (k + 1) for _ in range(n)]
        sell = [[0] * (k + 1) for _ in range(n)]

        buy[0][0], sell[0][0] = -prices[0], 0
        for i in range(1, k + 1):
            buy[0][i] = sell[0][i] = float("-inf")

        for i in range(1, n):
            buy[i][0] = max(buy[i - 1][0], sell[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i]);

        return max(sell[n - 1])
