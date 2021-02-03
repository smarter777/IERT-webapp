class Solution:
    """
    状态」，也就是原问题和子问题中会变化的变量 amount
    「选择」，也就是导致「状态」产生变化的行为 硬币面值
    明确 dp 函数/数组的定义 => dp 数组的定义：当目标金额为 i 时，至少需要 dp[i] 枚硬币凑出。

    1 + dp(n - coin) dp(n) 要凑出金额 n，至少要 dp(n) 个硬币
    dp(n) = 1 + dp(n-coin) 要凑出金额n,只需要dp(n-coin) + 1枚面值为coin的硬币
    说不定原本选定的res 就已经是最小的了-> min(res, 1 + dp(n-coin))
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 数组大小为 amount + 1，初始值也为 amount + 1
        dp = [amount+1] *(amount+1)

        # base case
        dp[0] = 0
        # 外层 for 循环在遍历所有状态的所有取值
        for i in range(len(dp)):
            # 内层 for 循环在求所有选择的最小值
            for coin in coins:
                if i-coin < 0: continue
                else:
                    dp[i] = min(dp[i], 1+dp[i-coin])
        return -1 if dp[amount] == amount +1 else dp[amount]

class Solution:
    """
    labuladong 动态规划模板->N 叉树的遍历问题
    ![](http://cdn.pic.mtianyan.cn/blog_img/20210202234638.png)

    # 定义：要凑出金额 n，至少要 dp(n) 个硬币
    def dp(n):
        # 做选择，选择需要硬币最少的那个结果
        for coin in coins:
            res = min(res, 1 + dp(n - coin))
        return res

    # 题目要求的最终结果是 dp(amount)
    return dp(amount)
    """

    def coinChange(self, coins: List[int], amount: int):
        # 备忘录
        memo = dict()

        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo: return memo[n]
            # base case
            if n == 0: return 0
            if n < 0: return -1

            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                # 子问题无解，跳过
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)

            # 记入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]

        return dp(amount)

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
