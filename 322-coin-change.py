class Solution:
    """
    labuladong 动态规划模板->N 叉树的遍历问题
    ![](http://cdn.pic.mtianyan.cn/blog_img/20210202234638.png)
    """

    def coinChange(self, coins: List[int], amount: int):

        def dp(n):
            if n == 0: return 0
            if n < 0: return -1

            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                # 子问题无解，跳过
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)
            return res if res != float('INF') else -1

        return dp(amount)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 自底向上
        # dp[i] 表示金额为i需要最少的硬币
        # dp[i] = min(dp[i], dp[i - coins[j]]) j所有硬币

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = min(dp[i - c] if i - c >= 0 else float("inf") for c in coins) + 1
        return dp[-1] if dp[-1] != float("inf") else -1


class Solution:
    """
    自顶向下
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        import functools
        @functools.lru_cache(None)
        def helper(amount):
            if amount == 0:
                return 0
            return min(helper(amount - c) if amount - c >= 0 else float("inf") for c in coins) + 1

        res = helper(amount)
        return res if res != float("inf") else -1


class Solution:
    """
    BFS
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        from collections import deque
        queue = deque([amount])
        step = 0
        visited = set()
        while queue:
            n = len(queue)
            for _ in range(n):
                tmp = queue.pop()
                if tmp == 0:
                    return step
                for coin in coins:
                    if tmp >= coin and tmp - coin not in visited:
                        visited.add(tmp - coin)
                        queue.appendleft(tmp - coin)
            step += 1
        return -1


class Solution:
    """
    dfs
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        self.res = float("inf")

        def dfs(i, num, amount):
            if amount == 0:
                self.res = min(self.res, num)
                return
            for j in range(i, len(coins)):
                # 剩下的最大值都不够凑出来了
                if (self.res - num) * coins[j] < amount:
                    break
                if coins[j] > amount:
                    continue
                dfs(j, num + 1, amount - coins[j])

        for i in range(len(coins)):
            dfs(i, 0, amount)

        return self.res if self.res != float("inf") else -1
