class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None

            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]

            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left,
                                    inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1,
                                     inorder_right)
            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(pre_left, pre_right, in_left, in_right):
            # 终止条件
            if pre_left > pre_right:
                return None
            # 前序根下标
            pre_root = preorder[pre_left]
            # 中序根下标
            in_root = index[pre_root]

            root = TreeNode(pre_root)

            len_left = in_root - in_left

            root.left = myBuildTree(pre_left + 1, pre_left + len_left, in_left, in_root - 1)
            root.right = myBuildTree(pre_left + len_left + 1, pre_right, in_root + 1, in_right)
            return root

        n = len(preorder)
        index = {ele: i for i, ele in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        x = preorder.pop(0)
        node = TreeNode(x)
        i = inorder.index(x)

        node.left = self.buildTree(preorder[:i], inorder[:i])
        node.right = self.buildTree(preorder[i:], inorder[i + 1:])
        return node


class Solution:
    """
    未解决，有问题的解法
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        in_map = dict(enumerate(inorder))
        in_map = {value: key for key, value in in_map.items()}
        print(in_map)
        self._buildTree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, in_map)

    # 构建一棵pre:start->end in:start->end 的树
    def _buildTree(self, preorder, pre_start, pre_end, inorder, in_start, in_end, in_map):
        root = TreeNode(preorder[pre_start])
        in_root = in_map.get(root.val)
        nums_left = in_root - in_start

        root.left = self._buildTree(preorder, pre_start + 1, pre_start + nums_left, inorder, in_start, in_root - 1,
                                    in_map)
        root.right = self._buildTree(preorder, pre_start + nums_left + 1, pre_end, inorder, in_root + 1, in_end, in_map)
        return root
