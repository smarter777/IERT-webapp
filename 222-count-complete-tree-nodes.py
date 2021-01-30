class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        lh, rh = self.__getHeight(root.left), self.__getHeight(root.right)
        if lh == rh:  # 左右子树高度相同，说明左子树必满 则节点数=左子树节点 + root节点(=1) + 递归找右子树
            return (pow(2, lh) - 1) + 1 + self.countNodes(root.right)
        else:  # 左子树比右子树高，说明右子树必满 同理
            return (pow(2, rh) - 1) + 1 + self.countNodes(root.left)

    def __getHeight(self, root):
        ret = 0
        while root:
            ret += 1
            root = root.left
        return ret

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def depth(root):
            if root == None:
                return 0
            return depth(root.left) + 1

        if root == None:
            return 0

        leftDepth = depth(root.left)
        rightDepth = depth(root.right)
        if leftDepth == rightDepth:
            #last note in right
            return 1 + pow(2,leftDepth) -1  + self.countNodes(root.right)
        else:
            return 1 + self.countNodes(root.left) + pow(2,rightDepth) - 1


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.cnt = 0

        def helper(root):
            if not root:
                return 0
            self.cnt += 1
            helper(root.left)
            helper(root.right)

        helper(root)
        return self.cnt

class Solution(object):
    # 本题核心就在于ret = 前h-1层的节点数(用公式求) + 最后一层节点数
    # 而最后一层的节点数 = 左侧节点数(依然用公式求) + 右侧节点数(就=1)
    def countNodes(self, root):
        if not root:
            return 0
        h = self.depth(root)
        cur, ret = root, 0
        while cur:
            # 左右子树高度相同，说明左子树肯定满，右子树可能满也可能不满
            if self.depth(cur.left) == self.depth(cur.right):
                # 这个是针对最后一个节点,画图就明白了
                if self.depth(cur.left) == 0:
                    ret += 1
                    break
                # 此时左子树肯定是满树，那么加上左子树(最后一层)的所有节点
                ret += int(math.pow(2, self.depth(cur.left) - 1))
                cur = cur.right
            else:
                cur = cur.left
        # 退出while说明最后一层的节点已经统计完，现在再根据公式加上前面h-1层的节点数
        ret += int(math.pow(2, h - 1)) - 1
        return ret

    def depth(self, root):
        level = 0
        while root:
            level += 1
            root = root.left
        return level