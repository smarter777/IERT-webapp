class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        中序遍历
        """
        self.pre = TreeNode(-float(inf))
        self.front,self.back = None, None
        self.recursion(root)
        self.front.val,self.back.val = self.back.val,self.front.val
    def recursion(self,cur):
        if not cur: return
        self.recursion(cur.left)
        if not self.front and self.pre.val > cur.val:
            self.front = self.pre
        if self.front and self.pre.val > cur.val:
            self.back = cur
        self.pre = cur
        self.recursion(cur.right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def recoverTree(self, root: TreeNode) -> None:
        """
        中序遍历，结果中如果有一个降序对，说明该两个node需交换；若有两个降序对，说明第一对的前一个node和第二对的后一个node需要交换。
        """
        self.mid_traverse(root)
        node1 = None
        node2 = None
        for i in range(len(self.res) - 1):
            if self.res[i].val > self.res[i + 1].val and node1 == None:
                node1 = self.res[i]
                node2 = self.res[i + 1]
            elif self.res[i].val > self.res[i + 1].val and node1 != None:
                node2 = self.res[i + 1]

        node1.val, node2.val = node2.val, node1.val

    def mid_traverse(self, root):
        if root is not None:
            self.mid_traverse(root.left)
            self.res.append(root)
            self.mid_traverse(root.right)