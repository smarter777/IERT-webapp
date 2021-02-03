# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        self.one_side_max(root)
        return self.ans

    """
   最大路径和：根据当前节点的角色，路径和可分为两种情况：
   一：以当前节点为根节点
   1.只有当前节点
   2.当前节点+左子树
   3.当前节点+右子书
   4.当前节点+左右子树    
   这四种情况的最大值即为以当前节点为根的最大路径和此最大值要和已经保存的最大值比较，得到整个树的最大路径值

   二：当前节点作为父节点的一个子节点
   和父节点连接的话则需取【单端的最大值】
   1.只有当前节点
   2.当前节点+左子树
   3.当前节点+右子书
   这三种情况的最大值    
   """

    def one_side_max(self, root):
        if not root:
            return 0
        left = max(0, self.one_side_max(root.left))
        right = max(0, self.one_side_max(root.right))
        self.ans = max(self.ans, left + right + root.val)
        return max(left, right) + root.val

