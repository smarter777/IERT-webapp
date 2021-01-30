# https://leetcode-cn.com/problems/integer-break/solution/zheng-shu-chai-fen-by-leetcode-solution/
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)

        dp[0] = dp[1] = 0
        # 思考点是dp[i]对应的是把i分成两个以上的数所得到的的最大积,i可以分为i-j和j, 那么,最大值可能就是i-j不再分了,或者在继续分
        for i in range(2, n+1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i-j), j * dp[i-j])
        return dp[n]

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]

class Solution:
    """
    求函数y=(n/x)^x(x>0)的最大值，可得x=e时y最大，但只能分解成整数，故x取2或3，由于6=2+2+2=3+3，显然2^3=8<9=3^2,故应分解为多个3
    """
    def integerBreak(self, n: int) -> int:
        if(n == 2):
            return 1
        if(n == 3):
            return 2
        a = 1
        while(n > 4):
            n = n - 3
            a = a * 3
        return a * n
