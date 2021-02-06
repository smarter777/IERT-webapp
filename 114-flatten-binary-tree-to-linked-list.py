class Solution:
    """
    前序遍历
    """

    def flatten(self, root: TreeNode) -> None:
        preorderList = list()

        def preorderTraversal(root: TreeNode):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)

        preorderTraversal(root)
        print(preorderList)
        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return root
        # 先把左右子树捋直
        self.flatten(root.left)
        self.flatten(root.right)

        tmp = root.right  # 把捋直的右子树备份一下
        root.right = root.left  # 把捋直的左子树放到右边
        root.left = None  # 记得把左子树置空
        while (root.right):  # 找到现在右子树的最后一个node
            root = root.right
        root.right = tmp  # 把捋直的原来的右子树接上去