class Solution:
    """
    状态压缩
    把DP table 的大小从 n 缩小到 2
    一般来说是把一个二维的 DP table 压缩成一维，即把空间复杂度从 O(n^2) 压缩到 O(n)
    """
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        # 只需要之前两个状态
        prev, cur = 1, 1
        for i in range(3, n+1):
            total = prev + cur
            prev = cur
            cur = total
        return cur


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        dp = [0] * (n+1)
        dp[1] = dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

class Solution:
    def fib(self, n: int) -> int:
        memo = [0] * (n + 1)  # 备忘录全初始化为 0
        return self.helper(memo, n)  # 进行带备忘录的递归

    def helper(self, memo, n):
        # base case
        if n == 0:
            return 0
        elif n == 1:
            return 1
        # 已经计算过
        if memo[n] != 0:
            return memo[n]
        memo[n] = self.helper(memo, n - 1) + self.helper(memo, n - 2)
        return memo[n]


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        res = [0,1]
        for i in range(2, n+1):
            res.append(res[i-1]+res[i-2])
        return res[-1]


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        p, q, r = 0, 0, 1
        for i in range(2, n + 1):
            p, q = q, r
            r = p + q

        return r


