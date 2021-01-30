class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """
        深度优先搜索
        """

        def dfs(root: TreeNode, prevTotal: int) -> int:
            if not root:
                return 0
            total = prevTotal * 10 + root.val
            if not root.left and not root.right:
                return total
            else:
                return dfs(root.left, total) + dfs(root.right, total)

        return dfs(root, 0)

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        paths = []          # 用于存储所有路径上的数字
        def dfs(root, path=''):
            if not root:
                return
            path += str(root.val)           # 取节点数字
            if not root.left and not root.right:
                paths.append(int(path))     # 如果遍历到底，则将路径上的数字保存
            dfs(root.left, path)
            dfs(root.right, path)
            path = path[:-1]                # 当前的路径走到最深后，需退回一个节点再向其他分支遍历
        dfs(root)
        return sum(paths)

class Solution:
    """
    https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/solution/qiu-gen-dao-xie-zi-jie-dian-shu-zi-zhi-he-by-leetc/

    广度优先搜索
    """

    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        total = 0
        nodeQueue = collections.deque([root])
        numQueue = collections.deque([root.val])

        while nodeQueue:
            node = nodeQueue.popleft()
            num = numQueue.popleft()
            left, right = node.left, node.right
            if not left and not right:
                total += num
            else:
                if left:
                    nodeQueue.append(left)
                    numQueue.append(num * 10 + left.val)
                if right:
                    nodeQueue.append(right)
                    numQueue.append(num * 10 + right.val)

        return total



