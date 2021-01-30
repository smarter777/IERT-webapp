class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(root, total):
            if not root:
                return
            total -= root.val
            path.append(root.val)
            if not root.left and not root.right and total == 0:
                res.append(path[:])
            dfs(root.left, total)
            dfs(root.right, total)
            path.pop()

        dfs(root, sum)
        return res


from collections import deque


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []

        paths = deque([[root, [], targetSum]])
        results = []

        while paths:
            node, curr_path, curr_sum = paths.popleft()

            curr_path += [node.val]
            curr_sum -= node.val
            if not node.left and not node.right and not curr_sum:
                results.append(curr_path)
            if node.left:
                paths.append([node.left, curr_path.copy(), curr_sum])
            if node.right:
                paths.append([node.right, curr_path.copy(), curr_sum])

        return results


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []

        def dfs(root, tmp, sum):
            nonlocal res
            if not root:
                return

            sum -= root.val
            if not root.left and not root.right and sum == 0:
                res.append(tmp + [root.val])
            dfs(root.left, tmp + [root.val], sum)
            dfs(root.right, tmp + [root.val], sum)
            return res

        dfs(root, [], sum)
        return res
