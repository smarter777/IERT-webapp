class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
            排列组合思路
             ans = ((m-1 + n-1))!/(m-1)!(n-1)!
        """

        def factor(num):
            if num < 2:
                return 1
            res = 1
            for i in range(1, num + 1):
                res *= i
            return res

        ans = factor(m + n - 2) // (factor(m - 1) * factor(n - 1))
        return ans


class Solution(object):
    """
    动态规划思路
    """
    def uniquePaths(self, m, n):
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = 0
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
