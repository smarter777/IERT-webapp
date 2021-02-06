from typing import List


class Solution:
    def searchR(self, nums: List[int], target: int) -> int:
        return self._search(nums, 0, len(nums) - 1, target)

    def _searchR(self, nums, l, r, target):
        if l > r:
            return -1
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            # 去左边找
            return self._search(nums, l, mid - 1, target)
        elif nums[mid] < target:
            return self._search(nums, mid + 1, r, target)

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                # 去左边找
                r = mid - 1
            else:
                l = mid + 1
        return -1


def left_bound(nums, target):
    if not nums: return -1
    left = 0
    right = len(nums)

    # [left, right)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            print("mid", mid)
            right = mid
        elif nums[mid] < target:
            print("mid<", mid)
            left = mid + 1
        elif nums[mid] > target:
            print("mid>", mid)
            right = mid
    return left


if __name__ == '__main__':
    print(left_bound([1, 2, 2, 2, 3], 2))
