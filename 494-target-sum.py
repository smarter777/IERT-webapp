class Solution:
    """
    作者：qsctech-sange
    链接：https://leetcode-cn.com/problems/target-sum/solution/python-dfs-xiang-jie-by-jimmy00745/
    动态规划
    """
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums) < S or (sum(nums) + S) % 2 == 1: return 0
        P = (sum(nums) + S) // 2
        dp = [1] + [0 for _ in range(P)]
        for num in nums:
            for j in range(P,num-1,-1):dp[j] += dp[j - num]
        return dp[P]

class Solution:
    """
    dfs
    作者：qsctech-sange
    链接：https://leetcode-cn.com/problems/target-sum/solution/python-dfs-xiang-jie-by-jimmy00745
    """
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        d = {}
        def dfs(cur, i, d):
            if i < len(nums) and (cur, i) not in d: # 搜索周围节点
                d[(cur, i)] = dfs(cur + nums[i], i + 1, d) + dfs(cur - nums[i],i + 1, d)
            return d.get((cur, i), int(cur == S))
        return dfs(0, 0, d)
