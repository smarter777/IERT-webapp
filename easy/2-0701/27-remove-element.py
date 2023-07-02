from typing import List


class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j