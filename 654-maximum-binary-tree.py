# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        # # 一、递归的方法：时间复杂度O(n^2),空间复杂度O(n)
        # if not nums:                    # 递归终止条件，当结点左/右子树为空
        #     return None
        # # elif len(nums) == 1:          # 叶结点这两句base case 可不写
        # #     return TreeNode(nums[0])

        # max_num = max(nums)              # 用max（）方法取出本次递归前数组的最大值
        # max_index = nums.index(max_num)  # 用index()方法取出本次递归数组最大值的位置下标
        # root = TreeNode(max_num)         # 将本次递归数组的最大值元素转化为二叉树的根结点
        # root.left = self.constructMaximumBinaryTree(nums[:max_index])  # 继续递归本次递归数组的左子树
        # root.right = self.constructMaximumBinaryTree(nums[max_index+1:]) # 继续递归本次递归数组的右子树
        # return root   # 返回本次递归的根结点到递归栈，程序执行结束返回的是整个二叉树数组（每个结点做根结点只一次）

        # 技巧：写递归代码时，按照原数组作为本次递归去写就行。其后的nums是随递归动态变化的，代码会自动进行下去，不用管。
        # root.left和root.right分别是本次递归跟的左右结点，分别是左右子树的根，按照树的数据结构，也代表了左右子树。

        # 二、单调栈：递减栈，从大到小存储。 看官方题解的单调栈
        # 寻找左侧第一个大于该节点的值和右侧第一个大于该节点的值，取两者最大的值作为父节点
        # 没有左边界，只能找右边界，自己作为左孩子节点

        # root is maximum number
        # stack  => indices
        # Time complexity : O(N)
        # Space complexity: O(N)

        if nums == []: return None  # corner case
        stack = []  # 递减栈，存放遍历当前位置前入栈的元素（树结点）。这里stack是树结点不是下标。
        for num in nums:
            node = TreeNode(num)  # 数组元素转化成树结点，不然无法加left和right字段。
            tmp = None  # 要有，之后更新，否则42句报错
            while stack and num > stack[-1].val:  # 此时可以探讨遍历的数组结点、栈顶、栈顶弹出后的新栈顶的父子关系
                tmp = stack.pop()  # 可能多次弹出，直至新栈顶大于num
            if tmp: node.left = tmp  # if是指非None。弹出的栈顶比遍历的结点小，且在数组中位于数组的左边，故作为node的左孩子
            if stack != []:  # 上面弹出后栈内不空，新的栈顶肯定比当前遍历的结点node大，且node位于栈顶的右端，故右孩子
                stack[-1].right = node  # 此时新栈顶比遍历的num大了，遍历的结点做新栈顶的右孩子
            stack.append(node)  # 遍历的当前树结点小于栈顶时直接入栈，大于时经过上面的while循环后入栈

        while len(stack) != 1:  # 37句遍历完栈内一定还有元素（最起码最大的树根还在栈底），不等于1就是排除栈底只有树根
            tmp = stack.pop()  # 逐一弹出（先弹出的是小的）
            stack[-1].right = tmp  # 弹出的作为新栈顶的右结点，因为栈内上面的元素小，且位于其下面元素的右边（数组内）
        return stack[-1]  # 最后的栈底最大就是root， 即树根。对于树，返回树根结点就是返回整棵树

        """
        # 注意：39、40、42、43句垂直对齐的逻辑。
        # 对于遍历的数组的第一个数，tmp=None, stack=[],保证直接执行第45句，入栈。
        # 第一个数以及随后连续递减的数必须直接入栈，才开始后续的。
        # 如果数组的前若干个数是单调减的，第40句不满足，tmp就是None，42句也不执行，接着执行第

        """


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return None if not nums else TreeNode(
            max(nums),  # 二叉树的根是数组 nums 中的最大元素
            self.constructMaximumBinaryTree(nums[:nums.index(max(nums))]),  # 左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树
            self.constructMaximumBinaryTree(nums[nums.index(max(nums)) + 1:]))  # 右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树
