class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        # 分三种情况讨论，根据二叉搜索树的性质，先递归找到等于key的节点root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # 找到节点后也要分情况讨论
            # 当只有0个或1个子节点时，直接并上子节点
            if not root.left or not root.right:
                root = root.left if root.left else root.right
            else:
                # 当两个子节点都存在时，保留左子树，让值等于右子树里最小的值
                cur = root.right
                while cur.left: cur = cur.left
                root.val = cur.val
                # 再对右子树递归删除已经被移上来的节点
                root.right = self.deleteNode(root.right, cur.val)

        return root


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        很优美的方法！找到右子树中的最小值，将要删除的节点替换为该值，然后在右子树中删除最小的那个节点。
        """

        if not root: return None;
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left or not root.right:
                root = root.left if root.left else root.right
            else:
                cur = root.right
                while cur.left: cur = cur.left
                root.val = cur.val
                root.right = self.deleteNode(root.right, cur.val)

        return root;


class Solution:

    def findSuc(self, cur: TreeNode):
        while cur.left:
            cur = cur.left
        return cur.val

    def findPre(self, cur: TreeNode):
        while cur.right:
            cur = cur.right
        return cur.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        if not root:
            return None

        if root.val == key:

            if root.right:  # 若右子树不为空（包含:1、有两个子节点2、仅有右子节点）
                root.val = self.findSuc(root.right)  # 找到右子树的最小值，交换
                root.right = self.deleteNode(root.right, root.val)  # 并删除右子树的最小节点
            elif root.left:  # 仅有左子节点
                root.val = self.findPre(root.left)  # 找到左子树的最大值，交换
                root.left = self.deleteNode(root.left, root.val)  # 并删除左子树的最大节点
            else:
                root = None  # 没有子节点

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root




