from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:  # 当新元素出现时
                i += 1  # 存储元素的数组指针后移
                nums[i] = nums[j]  # 同时存入新元素
        return i + 1


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != nums[i]:
                # 如果不等于上一个值
                nums[i+1] = nums[j]
                i += 1
            j += 1
        return i+1
