# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    返回一个大小为 2 的数组 arr
    arr[0] 表示不抢 root 的话，得到的最大钱数
    arr[1] 表示抢 root 的话，得到的最大钱数
    """

    def rob(self, root: TreeNode) -> int:
        def _rob(root):
            if not root: return 0, 0

            ls, ln = _rob(root.left)
            rs, rn = _rob(root.right)

            # 抢,下家就不能抢了
            rob = root.val + ln + rn
            # 不抢，下家可抢可不抢，取决于收益大小
            not_rob = max(ls, ln) + max(rs, rn)
            return rob, not_rob

        return max(_rob(root))

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


