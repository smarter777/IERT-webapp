# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        """
        作者：zedong
        链接：https://leetcode-cn.com/problems/find-duplicate-subtrees/solution/python-di-gui-shu-chu-zi-shu-xie-fa-by-zedong/
        你想知道以自己为根的子树是不是重复的，是否应该被加入结果列表中

        1、以我为根的这棵二叉树（子树）长啥样？

        2、以其他节点为根的子树都长啥样？

        # 标准后序代码

        // 先算出左右子树有多少节点
        int left = count(root.left);
        int right = count(root.right);
        /* 后序遍历代码位置 */
        // 加上自己，就是整棵二叉树的节点数
        int res = left + right + 1;
        """
        res = []
        counter = collections.Counter()

        def traverse(root):
            if not root: return '#'
            left = traverse(root.left)
            right = traverse(root.right)
            chain = left + ',' + right + ',' + str(root.val)
            counter[chain] += 1
            if counter[chain] == 2: res.append(root)
            return chain

        traverse(root)
        return res


