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
                dic[sidx, target] = func(sidx + 1, target - A[sidx]) or func(sidx + 1, target)  # 顺序反写 1100 ms + 141.7 MB
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
            return  False

        ac = sum(nums)
        if ac % 2 == 1:
            return  False

        res_ = ac / 2
        # 利用集合记录各种组合下来的和
        d = set()
        #最开始，什么都不取。这也是为了后面，对应不取某个数字的操作
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