# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = collections.deque()
        queue.append(root)
        # root 本身就是一层，depth 初始化为 1
        depth = 1
        while queue:
            # 将当前队列中的所有节点向四周扩散
            for i in range(len(queue)):
                cur = queue.popleft()
                # 判断是否到达终点
                if not cur.left and not cur.right:
                    return depth

                # 将 cur 的相邻节点加入队列
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            # 这里增加步数
            depth += 1
        return depth

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