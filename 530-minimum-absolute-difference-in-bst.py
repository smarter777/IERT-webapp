class Solution:
    """
    本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同
    """

    def getMinimumDifference(self, root: TreeNode) -> int:
        def dfs(node):
            if node:
                dfs(node.left)
                self.ans = min(abs(self.ans), abs(node.val - self.prev))
                self.prev = node.val
                dfs(node.right)

        self.prev = float('-inf')
        self.ans = float('inf')
        dfs(root)
        return self.ans


class Solution:
    """
    非递归
    """

    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root: return None
        pre = -1
        cur = root
        stack = []
        ans = float('inf')
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre != -1:
                    ans = min(ans, abs(cur.val - pre))
                pre = cur.val
                cur = cur.right
        return ans
