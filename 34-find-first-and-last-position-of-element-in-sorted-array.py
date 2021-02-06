class Solution:
    """
    https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/zai-pai-xu-shu-zu-zhong-cha-zhao-yuan-su-de-di-3-4/
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index = self.search(nums, target, True)
        right_index = self.search(nums, target, False) - 1
        if left_index <= right_index and right_index < len(nums) and nums[left_index] == target and nums[
            right_index] == target:
            return [left_index, right_index]
        else:
            return [-1, -1]

    def search(self, nums, target, lower):
        l = 0
        r = len(nums) - 1
        ans = len(nums)
        while l <= r:
            mid = (l + r) // 2
            if (nums[mid] > target) or (lower and nums[mid] >= target):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans


