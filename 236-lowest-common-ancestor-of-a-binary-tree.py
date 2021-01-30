class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        if root == p or root == q: return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if not left and not right:
            return None

        return right if not left else left


class Solution:
    """
    https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
    两个节点 p,q 分为两种情况：

    p 和 q 在相同子树中
    p 和 q 在不同子树中
    从根节点遍历，递归向左右子树查询节点信息
    递归终止条件：如果当前节点为空或等于 p 或 q，则返回当前节点

    递归遍历左右子树，如果左右子树查到节点都不为空，则表明 p 和 q 分别在左右子树中，因此，当前节点即为最近公共祖先；
    如果左右子树其中一个不为空，则返回非空节点
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root


'''(递归) O(n)O(n)

当我们用递归去做这个题时不要被题目误导，应该要明确一点
这个函数的功能有三个：给定两个节点 pp 和 qq

如果 pp 和 qq 都存在，则返回它们的公共祖先；
如果只存在一个，则返回存在的一个；
如果 pp 和 qq 都不存在，则返回NULL
本题说给定的两个节点都存在，那自然还是能用上面的函数来解决
'''


# 上面这段说明是非常关键的，帮助我们说明这个函数到底是怎么定义，怎么说明的
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 有了上面的函数的说明之后自己coding一遍
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        else:
            return root


class Solution:
    """
    https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/xiong-mao-shua-ti-python3-hui-su-2tiao-lu-jing-sha/
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def back(node, path, target, res):
            if not node:
                return
            if node == target:
                path.append(node)
                res.extend(path[:])  # 注意用[:],即浅拷贝
                return
            path.append(node)
            back(node.left, path, target, res)  # 回溯
            back(node.right, path, target, res)
            path.pop()  # 记得恢复状态

        res_p = []  # 两个变量，分别存储从根到目标点的路径
        res_q = []
        back(root, [], p, res_p)
        back(root, [], q, res_q)
        # 让 res_p 存储路径较小的那个，方便下面遍历查找操作
        if len(res_p) > len(res_q):
            res_p, res_q = res_q, res_p
        for i in range(len(res_p)):
            if res_p[i] != res_q[i]:
                if i > 0:
                    return res_p[i - 1]
                elif i == 0:
                    return res_p[i]
        return res_p[-1]
