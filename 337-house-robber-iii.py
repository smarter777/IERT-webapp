class Solution:

    def rob(self, root: TreeNode) -> int:
        def _rob(root):
            if not root: return 0, 0

            ls, ln = _rob(root.left)
            rs, rn = _rob(root.right)

            return root.val + ln + rn, max(ls, ln) + max(rs, rn)

        return max(_rob(root))

class Solution:
    """
    对于一个以 node 为根节点的二叉树而言，如果尝试偷取 node 节点，那么势必不能偷取其左右子节点，然后继续尝试偷取其左右子节点的左右子节点。

    如果不偷取该节点，那么只能尝试偷取其左右子节点。

    比较两种方式的结果，谁大取谁。

     //尝试对以 node 为根节点的二叉树进行偷取，返回能偷取的最大值
     int tryRob(LinkedList::TreeNode* node)
    """
    def rob(self, root: TreeNode) -> int:
            def _rob(root):
                if not root: return 0, 0  # 偷，不偷

                left = _rob(root.left)
                right = _rob(root.right)
                # 偷当前节点, 则左右子树都不能偷
                v1 = root.val + left[1] + right[1]
                # 不偷当前节点, 则取左右子树中最大的值
                v2 = max(left) + max(right)
                return v1, v2

            return max(_rob(root))


