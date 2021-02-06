from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]  # 题目要求的索引是从 1 开始的
            elif numbers[l] + numbers[r] < target:
                l += 1  # 让 sum 大一点
            elif numbers[l] + numbers[r] > target:
                r -= 1  # 让 sum 小一点


class Solution:
    # 对撞指针
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
