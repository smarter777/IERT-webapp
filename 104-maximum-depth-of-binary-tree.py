class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            ret = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
            return ret


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftdeep = self.maxDepth(root.left)
        rightdeep = self.maxDepth(root.right)
        return max(leftdeep, rightdeep) + 1


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        flag = 0
        while stack:
            temp = []
            for res in stack:

                if res.left:
                    temp.append(res.left)
                if res.right:
                    temp.append(res.right)
            stack = temp
            flag += 1
        return flag
