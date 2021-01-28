class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        levelOrder = list()
        if not root:
            return levelOrder

        q = collections.deque([root])
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
            levelOrder.append(level[-1])

        return levelOrder
