from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        // Sorting
        // Time Complexity: O(nlogn)
        // Space Complexity: O(1)
        """
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()


