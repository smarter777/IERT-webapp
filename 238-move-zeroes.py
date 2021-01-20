from typing import List


class Solution4:
    """
    48 ms
    // 原地(in place)解决该问题
    // 时间复杂度: O(n)
    // 空间复杂度: O(1)
    """

    def moveZeroes(self, nums: List[int]) -> None:
        k = 0  # nums中, [0...k)的元素均为非0元素
        # 遍历到第i个元素后,保证[0...i]中所有非0元素
        # 都按照顺序排列在[0...k)中
        # 同时, [k...i] 为 0
        for i in range(len(nums)):
            if nums[i]:
                if k != i:
                    # 如果k,i是一样的少一些交换操作
                    nums[k], nums[i] = nums[i], nums[k]
                k += 1


class Solution3:
    """
    28 ms
    // 原地(in place)解决该问题
    // 时间复杂度: O(n)
    // 空间复杂度: O(1)
    """

    def moveZeroes(self, nums: List[int]) -> None:
        k = 0  # nums中, [0...k)的元素均为非0元素
        # 遍历到第i个元素后,保证[0...i]中所有非0元素
        # 都按照顺序排列在[0...k)中
        # 同时, [k...i] 为 0
        for i in range(len(nums)):
            if nums[i]:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1


class Solution2:
    """
    56 ms
    // 原地(in place)解决该问题
    // 时间复杂度: O(n)
    // 空间复杂度: O(1)
    """

    def moveZeroes(self, nums: List[int]) -> None:
        k = 0  # nums中, [0...k)的元素均为非0元素
        # 假想数组前面有k个位置空着，都可以放非空值
        for i in range(len(nums)):
            # 遍历到第i个元素后,保证[0...i]中所有非0元素
            # 都按照顺序排列在[0...k)中
            if nums[i]:
                nums[k] = nums[i]
                k += 1
        # 将nums剩余的位置放置为0
        for i in range(k, len(nums)):
            nums[i] = 0


class Solution1:
    # 40 ms
    def moveZeroes(self, nums: List[int]) -> None:
        """
        // 时间复杂度: O(n)
        // 空间复杂度: O(n)
        """
        non_zero_list = []
        # 将nums中所有非0元素放入non_zero_list中
        non_zero_list = [one for one in nums if one]
        # 将non_zero_list中的所有元素依次放入到nums开始的位置
        for i in range(len(non_zero_list)):
            nums[i] = non_zero_list[i]
        # 将nums剩余的位置放置为0
        for i in range(len(non_zero_list), len(nums)):
            nums[i] = 0
