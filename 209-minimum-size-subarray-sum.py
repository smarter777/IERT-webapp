from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = 0
        r = -1  # nums[l...r]为我们的滑动窗口
        sum_total = 0
        res = len(nums) + 1
        while l < len(nums):  # 窗口的左边界在数组范围内,则循环继续
            if r + 1 < len(nums) and sum_total < s:  # 如果右边界还可以滑动,sum还可以再加一个
                sum_total += nums[r + 1]
                r += 1
            else:  # r已经到头 或者 sum >= s
                sum_total -= nums[l]
                l += 1
            if sum_total >= s:
                res = min(res, r - l + 1)
        if res == len(nums) + 1:
            return 0
        return res
