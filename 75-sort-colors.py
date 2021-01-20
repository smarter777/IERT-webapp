from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        // 三路快速排序的思想
        // 对整个数组只遍历了一遍
        // 时间复杂度: O(n)
        // 空间复杂度: O(1)
        """
        zero = -1  # [0...zero] == 0
        two = len(nums)  # [two...n-1] == 2
        i = 0
        while i < two:
            if nums[i] == 0:
                zero += 1
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1
            elif nums[i] == 1:
                i += 1
            else:  # num[i]==2
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        // 计数排序的思路
        // 对整个数组遍历了两遍
        // 时间复杂度: O(n)
        // 空间复杂度: O(k), k为元素的取值范围
        """
        count_list = [0 for i in range(3)]  # 存放0, 1, 2三个元素的频率
        for i in range(len(nums)):
            count_list[nums[i]] += 1
        index = 0
        for i in range(count_list[0]):
            nums[index] = 0
            index += 1
        for i in range(count_list[1]):
            nums[index] = 1
            index += 1
        for i in range(count_list[2]):
            nums[index] = 2
            index += 1
