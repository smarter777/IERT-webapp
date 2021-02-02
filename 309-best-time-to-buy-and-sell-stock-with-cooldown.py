class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        s0=0
        s1=float("-inf")
        s2=float("-inf")
        for i in range(n):
            s0,s1,s2=max(s0,s2),max(s1,s0-prices[i]),s1+prices[i]
        return max(s0,s2)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        # f[i][0]: 手上持有股票的最大收益
        # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
            f[i][1] = f[i - 1][0] + prices[i]
            f[i][2] = max(f[i - 1][1], f[i - 1][2])

        return max(f[n - 1][1], f[n - 1][2])


"""
class Solution {
    public int maxProfit(int[] prices) {
        if(prices == null || prices.length == 0){
            return 0;
        }
        //状态转移图：
        //       持股               不持股
        //     ↙-----、   卖出    ↙-----、
        //    持股-----↑--------→不持股---↑
        //      |                                                       
        //      |卖                                                     
        //      |出                                                  
        //      ↓                                                     
        //    冷冻期(期间什么都不能干，冷冻期结束后转为不持股状态) 
        //
        int[][] dp = new int[prices.length][3];
        //dp[i][x]第i天进入(处于)x状态（0.不持股，1.持股，2.冷冻期）
        //不持股
        dp[0][0] = 0;
        //持股
        dp[0][1] = -prices[0];
        //冷冻期
        dp[0][2] = 0;
        for(int i = 1;i < prices.length;i++){
            //第i天不持股可以从两种状态转移而来，1.第i-1天不持股，今天仍不买股票，保持不持股状态。2.冷冻期结束了，但是今天不买股票。
            dp[i][0] = Math.max(dp[i-1][0], dp[i-1][2]);
            //第i天持股可从两种状态转移而来，1.第i-1天不持股(包含昨天是冷冻期，冷冻期结束后转为不持股状态和昨天本身就不持股这两种情况)，今天买股票。2.第i-1天持股，今天不卖出，保持持股状态。
            dp[i][1] = Math.max(dp[i - 1][0] - prices[i], dp[i - 1][1]);
            //只有第i - 1天卖出了股票，第i天才处于冷冻期。
            dp[i][2] = dp[i-1][1] + prices[i];
        }
        //只有最后一天不持股（不持股状态）或者前一天已经卖掉了（今天为冷冻期）这两种情况手里是拿着钱的，最大值在二者中产生。
        return Math.max(dp[prices.length - 1][0], dp[prices.length - 1][2]);
    }
}
"""
