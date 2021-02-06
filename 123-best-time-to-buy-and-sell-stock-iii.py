class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        作者：edelweisskoko
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/yi-kan-jiu-dong-de-jian-dan-ti-jie-by-ed-0o3l/
        """
        if not prices:
            return 0

        dp0 = 0  # 一直不买
        dp1 = - prices[0]  # 到最后也只买入了一笔
        dp2 = float("-inf")  # 到最后买入一笔，卖出一笔
        dp3 = float("-inf")  # 到最后买入两笔，卖出一笔
        dp4 = float("-inf")  # 到最后买入两笔，卖出两笔

        for i in range(1, len(prices)):
            dp1 = max(dp1, dp0 - prices[i])
            # 前一天也是dp1状态，或者前一天是dp0状态，今天买入一笔变成dp1状态
            dp2 = max(dp2, dp1 + prices[i])
            # 前一天也是dp2状态，或者前一天是dp1状态，今天卖出一笔变成dp2状态
            dp3 = max(dp3, dp2 - prices[i])
            # 前一天也是dp3状态，或者前一天是dp2状态，今天买入一笔变成dp3状态
            dp4 = max(dp4, dp3 + prices[i])
            # 前一天也是dp4状态，或者前一天是dp3状态，今天卖出一笔变成dp4状态
        return max(dp0, dp2, dp4) # 最后一定是手里没有股票赚的钱最多，但不一定交易次数越多赚得越多，因此返回的是dp0，dp2，dp4的最大值

class Solution:
    """
    由于我们最多可以完成两笔交易，因此在任意一天结束之后，我们会处于以下五个状态中的一种
    未进行过任何操作； 利润 0
    只进行过一次买操作；buy1
    进行了一次买操作和一次卖操作，即完成了一笔交易； sell1
    在完成了一笔交易的前提下，进行了第二次买操作； buy2
    完成了全部两笔交易。 sell2
    """

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])  # 可以保持buy1, 也可以在未进行任何操作的前提下以price买入股票
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2
