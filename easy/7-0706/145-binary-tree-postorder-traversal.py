class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root: TreeNode):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)


        res = list()
        postorder(root)
        return res

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        stack=[]

        while root or stack:
            if root:
                res.insert(0,root.val)#中，每次插入到最前面
                stack.append(root)
                root=root.right#右
            else:
                tem=stack.pop()
                root=tem.left#左
        return res