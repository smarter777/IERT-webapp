class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        如果该二叉树的左子树不为空，则左子树上所有节点的值均小于它的根节点的值；
        若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值；它的左右子树也为二叉搜索树。
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        中序遍历为升序
        """
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True

