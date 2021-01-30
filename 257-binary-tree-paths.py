class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        paths = []
        if root.left:
            for i in self.binaryTreePaths(root.left):
                paths.append(str(root.val) + '->' + i)
        if root.right:
            for i in self.binaryTreePaths(root.right):
                paths.append(str(root.val) + '->' + i)
        return paths


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        def dfs(root,tmp):
            if not root:
                return
            # 如果是叶子节点，将 root.val 拼接到临时路径中
            if root and not (root.left or root.right):
                res.append(tmp+str(root.val))
                return
            # 如果当前节点不是叶子节点，将 root.val+"->" 拼接到临时路径中
            if root.left:
                dfs(root.left,tmp+str(root.val)+"->")
            # 如果当前节点不是叶子节点，将 root.val+"->" 拼接到临时路径中
            if root.right:
                dfs(root.right,tmp+str(root.val)+"->")
        dfs(root,"")
        return res


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        if not root:
            return paths
        num_queue = [root]
        path_queue = [str(root.val)]

        while num_queue:
            current = num_queue.pop(0)
            current_path = path_queue.pop(0)
            if current.left:
                num_queue.append(current.left)
                path_queue.append(current_path + '->' + str(current.left.val))
            if current.right:
                num_queue.append(current.right)
                path_queue.append(current_path + '->' + str(current.right.val))
            if not current.right and not current.left:
                paths.append(current_path)
        return paths


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res=[]
        if root is None:
            return res
        stack=[(root,'')]
        while stack:
            temp=stack.pop(0)
            node=temp[0]
            road=temp[1]
            if node.left is None and node.right is None:
                res.append(road+str(node.val))
            if node.left:
                stack.append((node.left,road+str(node.val)+"->"))
            if node.right:
                stack.append((node.right,road+str(node.val)+"->"))
        return res
