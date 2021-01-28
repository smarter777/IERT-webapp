# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levelOrder = list()
        if not root:
            return levelOrder

        q = collections.deque([root])
        count = 0
        while q:
            level = list()
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if count % 2:
                levelOrder.append(level[::-1])
            else:
                levelOrder.append(level)
            count += 1
        return levelOrder

