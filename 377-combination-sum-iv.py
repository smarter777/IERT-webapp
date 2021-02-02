class Solution:
    """
    https://leetcode-cn.com/problems/combination-sum-iv/solution/xi-wang-yong-yi-chong-gui-lu-gao-ding-bei-bao-wen-/

    一种规律解决背包问题
    """
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1,target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[target]

