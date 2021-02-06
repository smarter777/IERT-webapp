class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        首先，首尾房间不能同时被抢，那么只可能有三种不同情况：
        要么都不被抢；要么第一间房子被抢最后一间不抢；要么最后一间房子被抢第一间不抢。
        """
        n = len(nums)
        if n == 1: return nums[0]
        return max(self.rob_range(nums, 0, n - 2), self.rob_range(nums, 1, n - 1))

    def rob_range(self, nums: List[int], start, end) -> int:
        nums = nums[start:end + 1]
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
    """:cvar
    https://leetcode-cn.com/problems/house-robber-ii/solution/213-da-jia-jie-she-iidong-tai-gui-hua-jie-gou-hua-/
    """

    def rob(self, nums: [int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur

        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]


class Solution:
    def rob(self, nums: List[int]) -> int:
        ##房子排成了一个圆圈，则如果抢了第一家，就不能抢最后一家，因为首尾相连了，所以第一家和最后一家只能抢其中的一家，或者都不抢，
        ##那这里变通一下，如果把第一家和最后一家分别去掉，各算一遍能抢的最大值，然后比较两个值取其中较大的一个即为所求。

        def robOne(self, numsOne: List[int]) -> int:
            # 198题，打家劫舍一的代码
            ##dp[i] 表示 [0, i] 区间可以抢夺的最大值，对当前i来说，有抢和不抢两种互斥的选择，不抢即为 dp[i-1]（等价于去掉 nums[i] 只抢 [0, i-1] 区间最大值），抢即为 dp[i-2] + nums[i]（等价于去掉 nums[i-1]）。即选择两者中最大值为dp[i]
            dp = [0 for _ in numsOne]
            if len(numsOne) == 1:
                return numsOne[0]
            dp[0] = numsOne[0]
            dp[1] = max(numsOne[0], numsOne[1])
            for i in range(2, len(numsOne), 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + numsOne[i])
            return dp[-1]

        if not nums:  # 空数组
            return 0
        if len(nums) == 1:
            return nums[0]
        nums_0 = nums[1:]
        nums_n = nums[:len(nums) - 1]
        return max(robOne(self, nums_n), robOne(self, nums_0))
