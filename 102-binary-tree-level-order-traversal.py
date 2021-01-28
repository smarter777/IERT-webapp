class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:  # NOTE: 注意root可能为空
            return []
        res = []
        cur_nodes = [root]
        next_nodes = []
        res.append([i.val for i in cur_nodes])
        while cur_nodes or next_nodes:
            for node in cur_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            if next_nodes:
                res.append(
                    [i.val for i in next_nodes]
                )

            cur_nodes = next_nodes
            next_nodes = []
        return res


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []

        def layerorder(root, layer):
            if root != None:
                if layer >= len(ans):
                    ans.append([])
                ans[layer].append(root.val)
                layerorder(root.left, layer + 1)
                layerorder(root.right, layer + 1)

        layerorder(root, 0)
        return ans
