class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        print(dp)
        dp[0][0] = 1
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


class Solution:
    """
    作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/unique-paths/solution/bu-tong-lu-jing-by-leetcode-solution-hzjf/
    """

    def uniquePaths(self, m: int, n: int) -> int:
        # f(i,j) 表示从左上角走到 (i,j) 的路径数量
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(f)
        # f(0,0)=1
        for i in range(1, m):
            for j in range(1, n):
                # 如果向下走一步，那么会从 (i−1,j) 走过来；如果向右走一步，那么会从 (i,j−1) 走过来
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]


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
