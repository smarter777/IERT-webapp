class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return str(p) == str(q)


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            # 如果两个二叉树都为空，则两个二叉树相同。
            return True
        if not q or not p:
            # 如果两个二叉树中有且只有一个为空，则两个二叉树一定不相同。
            return False
        if q.val != p.val:
            # 如果两个二叉树都不为空，那么首先判断它们的根节点的值是否相同，若不相同则两个二叉树一定不同，
            return False
        # 若相同，再分别判断两个二叉树的左子树是否相同以及右子树是否相同。
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
