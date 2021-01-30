class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # null节点不参与比较
        if not root.left and root.right:
            return 1 + self.minDepth(root.right)
        # null节点不参与比较
        if not root.right and root.left:
            return 1 + self.minDepth(root.left)
        leftdeep = self.minDepth(root.left)
        rightdeep = self.minDepth(root.right)
        return min(leftdeep, rightdeep) + 1

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        res, queue = float("+inf"), collections.deque()
        queue.append((root, 1))
        while queue:
            cur, depth = queue.popleft()
            if depth >= res:
                continue
            if cur.left: queue.append((cur.left, depth+1))
            if cur.right: queue.append((cur.right, depth+1))
            if not cur.left and not cur.right:
                res = depth
        return res