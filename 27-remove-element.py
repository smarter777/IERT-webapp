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