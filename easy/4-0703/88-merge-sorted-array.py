from typing import List


class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        三指针 指针一p1、nums1有效元素尾部；指针二p2、nums2尾部；指针三p3、最终数组尾部

        1.当，p1 >= 0时，nums[p1],nums[p2]对比
        1.1 nums[p1]大，将nums[p1]放入p3位置。p1--,p3--
        1.2 nums[p2]大于等于nums[p1]，将nums[p2]放入p3位置。p2--,p3--
        2.当，p1<0时，将nums[p2]放入p3位置。p2--,p3--
        循环结束条件：p2<0
        """
        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p3 -= 1
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p3 -= 1
                p2 -= 1


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


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1.append(nums2[i])
        nums1.sort()


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 思路的重点一个是从后往前确定两组中该用哪个数字
        # 另一个是结束条件以第二个数组全都插入进去为止
        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        while p2 >= 0 or p1 >= 0:
            if p1 == -1:
                nums1[p3] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[p3] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                # 第一个数组更大
                nums1[p3] = nums1[p1]
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1
            p3 -= 1
