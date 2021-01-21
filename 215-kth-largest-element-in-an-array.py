from random import randrange
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


class Solution:
    # 利用快排思想
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self._findKthLargest(nums, 0, len(nums) - 1, k - 1)

    def _findKthLargest(self, nums, l, r, k):
        if l == r:
            return nums[l]

        p = self.partition(nums, l, r)

        if p == k:
            return nums[p]
        elif k < p:
            return self._findKthLargest(nums, l, p - 1, k)
        else:
            return self._findKthLargest(nums, p + 1, r, k)

    def partition(self, arr, l, r):
        # 生成[l,r]随机索引
        p = randrange(l, r)
        arr[l], arr[p] = arr[p], arr[l]
        # arr[l+1...lt) > p ; arr[lt...i) < p
        lt = l + 1
        for i in range(l + 1, r + 1):
            if arr[i] > arr[l]:
                arr[i], arr[lt] = arr[lt], arr[i]
                lt += 1

        arr[l], arr[lt - 1] = arr[lt - 1], arr[l]
        return lt - 1
