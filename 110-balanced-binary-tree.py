class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        https://leetcode-cn.com/problems/balanced-binary-tree/solution/ping-heng-er-cha-shu-by-leetcode-solution/
        自顶向下的递归
        """

        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        https://leetcode-cn.com/problems/balanced-binary-tree/solution/ping-heng-er-cha-shu-by-leetcode-solution/
        自底向上的递归
        """
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            #print(right, left)
            if abs(right - left) > 1:
                self.res = False
            return max(left, right) + 1
        helper(root)
        return self.res

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        附上一个我觉得很啰嗦的解法...但是我觉得树的递归大部分都可以这么套路的解决，相当于一个解题模版（初学数据结构的菜鸡
模版一共三步，就是递归的三部曲：
找终止条件：什么时候递归到头了？此题自然是root为空的时候，空树当然是平衡的。
思考返回值，每一级递归应该向上返回什么信息？参考我代码中的注释。
单步操作应该怎么写？因为递归就是大量的调用自身的重复操作，因此从宏观上考虑，只用想想单步怎么写就行了，左树和右树应该看成一个整体，即此时树一共三个节点：root，root.left，root.right。
https://leetcode-cn.com/problems/balanced-binary-tree/comments/
        """
