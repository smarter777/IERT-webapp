class Solution(object):
    """
    将树中所有节点的值写入数组，之后将数组排序。依次计算相邻数之间的差值，找出其中最小的值。
    """
    def minDiffInBST(self, root):
        vals = []
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        vals.sort()
        return min(vals[i+1] - vals[i]
                   for i in range(len(vals) - 1))


class Solution(object):
    """
    在二叉搜索树中，中序遍历会将树中节点按数值大小顺序输出。只需要遍历计算相邻数的差值，取其中最小的就可以了。
    """
    def minDiffInBST(self, root):
        def dfs(node):
            if node:
                dfs(node.left)
                self.ans = min(self.ans, node.val - self.prev)
                self.prev = node.val
                dfs(node.right)

        self.prev = float('-inf')
        self.ans = float('inf')
        dfs(root)
        return self.ans