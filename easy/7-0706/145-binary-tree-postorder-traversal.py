class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root: TreeNode):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        res = list()
        postorder(root)
        return res


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []

        while root or stack:
            if root:
                res.insert(0, root.val)  # 中，每次插入到最前面
                stack.append(root)
                root = root.right  # 右
            else:
                tem = stack.pop()
                root = tem.left  # 左
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)

        res = []
        dfs(root)
        return res
