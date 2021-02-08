class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums)
        if (target % 2 != 0):
            return False
        target //= 2
        pre = [False] * (target + 1)  # 表示到上一个物品为止的装包情况
        cur = [False] * (target + 1)  # 表述当前物品的装包情况
        pre[0] = True  # 将第一个物品可以装满的容量置为 True
        for i in range(1, target + 1):
            if (nums[0] == i):
                pre[i] = True
                break
        for i in range(1, n):
            for j in range(target + 1):
                if (j >= nums[i]):
                    # 可以装进去，装 或 不装
                    cur[j] = pre[j] or (pre[j - nums[i]])
                else:
                    # 不装进去
                    cur[j] = pre[j]
            if cur[target]:
                break
            pre = cur[:]
        return cur[-1]


class Solution:
    """
    dp[4][9] = true，其含义为：对于容量为 9 的背包，若只是用前 4 个物品，可以有一种方法把背包恰好装满
    """

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums)
        if (target % 2 != 0):
            # 和为奇数时，不可能划分成两个和相等的集合
            return False
        target //= 2
        dp = [[False] * (target + 1) for _ in range(n)]
        # base case
        dp[0][0] = True
        for i in range(1, target + 1):
            if (nums[0] == i):
                dp[0][i] = True
                break
        # dp[i][j] = x 表示，对于前 i 个物品，
        # 当前背包的容量为 j 时，若 x 为 true，
        # 则说明可以恰好将背包装满，若 x 为 false，则说明不能恰好将背包装满。
        for i in range(1, n):
            for j in range(target + 1):
                if (j >= nums[i]):
                    # 装入或不装入背包
                    # 你如果装了第 i 个物品，
                    # 就要看对于前i-1个物品的背包而言， 是否正好 剩余重量= 容量j - 当前物品nums[i-1]
                    dp[i][j] = dp[i - 1][j] or (dp[i - 1][j - nums[i]])
                else:
                    # 背包容量不足，不能装入第 i 个物品
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


class Solution:
    """
    dp[4][9] = true 对于容量为 9 的背包，若只是用前 4 个物品，可以有一种方法把背包恰好装满
    对于给定的集合中，若只对前 4 个数字进行选择，存在一个子集的和可以恰好凑出 9。

    我们想求的最终答案就是 dp[N][sum/2]
    base case 就是 dp[..][0] = true 和 dp[0][..] = false，
    因为背包没有空间的时候，就相当于装满了，而当没有物品可选择的时候，肯定没办法装满背包。

    对 dp[i][j] 得到以下状态转移
        你不把这第 i 个物品装入背包，那么是否能够恰好装满背包，取决于上一个状态 dp[i-1][j]，继承之前的结果
        你把这第 i 个物品装入了背包，那么是否能够恰好装满背包，取决于状态 dp[i-1][j-nums[i-1]]
        由于 i 是从 1 开始的，而数组索引是从 0 开始的，所以第 i 个物品的重量应该是 nums[i-1]
        dp[i - 1][j-nums[i-1]] 也很好理解：你如果装了第 i 个物品，
        就要看背包的剩余重量 j - nums[i-1] 限制下是否能够被恰好装满

        换句话说，如果 j - nums[i-1] 的重量可以被恰好装满，
        那么只要把第 i 个物品装进去，也可恰好装满 j 的重量；否则的话，重量 j 肯定是装不满的
    """

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [True] + [False] * target
        # base case dp[0] = true
        print(dp)
        for num in nums:
            for j in range(target, num - 1, -1):
                # j 应该从后往前反向遍历，因为每个物品（或者说数字）只能用一次，
                # 以免之前的结果影响其他的结果
                dp[j] |= dp[j - num]
            if dp[target]:
                break

        return dp[target]


class Solution:
    def canPartition(self, A: List[int]) -> bool:

        # public solution ...
        # 深度优先搜索

        dic = {0: True}

        def func(sidx, target):
            if target not in dic:
                dic[target] = False
                if target > 0:
                    for cidx in range(sidx, len(A)):
                        if func(cidx + 1, target - A[cidx]):
                            dic[target] = True
                            break
            return dic[target]

        target = sum(A)
        if target & 1: return False
        target //= 2
        return func(0, target)

        # public solution ... 52 ms ... 98 % ... 14.9 MB ... 49 %
        # 用 stack
        #  time: O(n^2)
        # space; O(n)

        target = sum(A)
        if target & 1: return False
        target //= 2
        A.sort(reverse=True)
        if A[0] > target: return False
        if A[0] == target: return True
        for i in range(1, len(A)):  # 尝试将每个 A[i] 与 A[0] 进行搭配
            stack = [A[0], A[i]]
            if sum(stack) == target:
                return True
            for j in range(i + 1, len(A)):
                stack.append(A[j])
                if sum(stack) > target:  # 使用 A[i+1:] 中的小数，不停的微调
                    stack.pop()
            if sum(stack) == target:
                return True
        return False

        # public solution ... 40 ms ... 100 % ... 14.9 MB ... 49 %
        # 看不懂这个算法
        #  time: O(n)
        # space: O(1)

        if len(A) < 2:
            return False
        total, result = 0, 1
        for a in A:
            total += a
            result = result | result << a
        if total & 1:
            return False
        target = total // 2
        if result & (1 << target):
            return True
        return False

        # public solution ... 40 ms ... 100 % ... 14.8 MB ... 50 %
        # 双指针
        #  time: O(n^2)
        # space: O(1)

        A.sort()
        tot = sum(A)
        if tot & 1 or A[-1] > tot // 2:
            return False
        target = tot // 2
        curr, l, r = 0, 0, len(A) - 1
        while l < r:
            if curr + A[r] < target:
                curr += A[r]
                r -= 1
            elif curr + A[r] == target or target - curr in A[l:r]:
                return True
            else:
                curr += A[l]
                l += 1
        return False

        # my solution ... 212 ms ... 94 % ... 33.4 MB ... 7 %
        # 深度优先搜索
        #  time: O(n*t)
        # space: O(n*t)

        dic = {}

        def func(sidx, target):  # 返回从 A[sidx:] 中找 target 的可能性
            if not target:
                return True
            if sidx == len(A) or target < A[sidx]:
                return False
            if (sidx, target) not in dic:
                dic[sidx, target] = func(sidx + 1, target - A[sidx]) or func(sidx + 1,
                                                                             target)  # 顺序反写 1100 ms + 141.7 MB
                # res = False
                # for cidx in range(sidx, len(A)):        # 4972 ms ... 0 % ... 35.9 MB ... 6 %
                #     if target < A[cidx]:
                #         break
                #     if func(cidx + 1, target - A[cidx]):
                #         res = True
                #         break
                # dic[sidx, target] = res
            return dic[sidx, target]

        A.sort()
        tot = sum(A)
        if tot % 2 or A[-1] > tot // 2:
            return False
        return func(0, tot // 2)


class Solution:
    # 讨论区看到的一种解法，很巧妙。
    def canPartition(self, nums: List[int]) -> bool:
        # 常规判定
        if len(nums) < 2:
            return False

        ac = sum(nums)
        if ac % 2 == 1:
            return False

        res_ = ac / 2
        # 利用集合记录各种组合下来的和
        d = set()
        # 最开始，什么都不取。这也是为了后面，对应不取某个数字的操作
        d.add(0)
        # 顺次取数字
        for num in nums:
            # 和既有的和操作，key = 0时，说明不取这个数，
            for k in list(d):
                r = num + k
                # 每次判定是否达标
                if r == res_:
                    return True
                # 计算的和加入字典
                d.add(r)
        return False


class Solution:
    """
    https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/fen-ge-deng-he-zi-ji-by-leetcode-solution/
    """

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]

        return dp[target]
