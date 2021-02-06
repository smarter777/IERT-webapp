class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)

        return second

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        dp = [0] * size
        # base
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # 第i(i>2)天，只能dp[i-2]
        for i in range(2, size):
            # 偷或不偷
            # 1. 偷 k 就不能偷k-1,偷窃总金额为前 k−2 间房屋的最高总金额与第 k 间房屋的金额之和。
            # 2. 不偷窃第 k 间房屋，偷窃总金额为前 k−1 间房屋的最高总金额
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[size - 1]

class Solution:
    def rob(self, nums):
        prev, cur = 0, 0
        # prev: dp[k-2]
        # cur: dp[k-1]
        # 每次循环，计算“偷到当前房子为止的最大金额”
        for num in nums:
            # dp[k] = max(dp[k-1], dp[k-2] + num)
            prev, cur = cur, max(prev + num, cur)
            # 循环结束时候，curr 表示dp[k], prev表示dp[k-1]

        return cur

        # # dp[2] = max(dp[1], dp[0] + nums[2])
        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # return max(dp)


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        巧妙的运用了python的逗号赋值的性质
        """
        last = 0
        now = 0
        for i in nums:
            # 这是一个动态规划问题
            # 动态规划。最大利益 = max（上家的最大利益，上家的上家的最大利益 + 当前家的利益）
            last, now = now, max(last + i, now)
        return now


class Solution:
    """
    动态规划 + 滚动数组
    https://leetcode-cn.com/problems/house-robber/solution/da-jia-jie-she-by-leetcode-solution/
    """

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[size - 1]
