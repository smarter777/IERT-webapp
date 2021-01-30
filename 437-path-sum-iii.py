class Solution:
    """
    今天学到了叫做双重递归的操作，这种题目需要从每个节点开始进行类似的计算，所以第一个递归用来遍历这些节点，这二个递归用来处理这些节点，进行深度优先搜索
    从543来的，比较类似
递归返回 possible 即该根节点的所有可能值，一层层往上加

收获：

递归过程记录全局变量（即答案），返回计算所需值
    """
    def pathSum(self, root: TreeNode, sum: int) -> int:
            self.ans = 0
            def allSum(root):
                if not root: return []      # 递归终点
                possible = [root.val]
                if root.val == sum: self.ans += 1   # 根 == sum
                left = allSum(root.left)
                right = allSum(root.right)
                for i in left:
                    temp = root.val + i     # 根 + 左可能值
                    possible.append(temp)
                    if temp == sum: self.ans += 1
                for i in right:
                    temp = root.val + i     # 根 + 右可能值
                    possible.append(temp)
                    if temp == sum: self.ans += 1
                return possible

            allSum(root)
            return self.ans


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0
        target = sum
        h = collections.defaultdict(int)
        self.countSum(root, 0, h, target)
        return self.count

    def countSum(self, root, cur_sum, h, target):
        if not root:
            return
        cur_sum += root.val
        if cur_sum == target:
            self.count += 1
        self.count += h[cur_sum - target]
        # print(self.count)
        h[cur_sum] += 1
        self.countSum(root.left, cur_sum, h, target)
        self.countSum(root.right, cur_sum, h, target)
        h[cur_sum] -= 1


class Solution:
    # 双递归

    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(root, presum):
            nonlocal sum_map
            nonlocal sum
            nonlocal ret
            # 终止条件
            if not root:
                return 0

            # 更新前缀和
            presum += root.val
            remain = presum - sum
            # 前缀和中 有几个相同的值就加几次
            if remain in sum_map:
                ret += sum_map[remain]

            # 更新前缀和 map
            x = sum_map.setdefault(presum, 0)
            sum_map[presum] = x + 1

            # 递归
            dfs(root.left, presum)
            dfs(root.right, presum)

            sum_map[presum] -= 1

        sum_map = {0: 1}
        ret = 0

        dfs(root, 0)
        return ret

