# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # 总是选择中间位置左边的数字作为根节点
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        else:
            mid = len(nums) // 2
            tn = TreeNode(nums[mid])
            nums1 = nums[0:mid]
            nums2 = nums[mid + 1:len(nums)]
            tn.left = self.sortedArrayToBST(nums1)
            tn.right = self.sortedArrayToBST(nums2)
        return tn


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        else:
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            nums1 = nums[0:mid]
            nums2 = nums[mid+1:len(nums)]
            root.left = self.sortedArrayToBST(nums1)
            root.right = self.sortedArrayToBST(nums2)
        return root