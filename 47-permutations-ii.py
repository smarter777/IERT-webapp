class Solution:
    """
    https://leetcode-cn.com/problems/permutations-ii/solution/hot-100-47quan-pai-lie-ii-python3-hui-su-kao-lu-zh/
    """

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]

        self.backtrack([], nums, check)
        return self.res

    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return

        for i in range(len(nums)):
            if check[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                continue
            check[i] = 1
            self.backtrack(sol + [nums[i]], nums, check)
            check[i] = 0


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Jan 20, 2021
        # 先做了第46题，看到题完全没思路。试图理解“回溯”中...
        nums.sort()
        self.res = []
        temp = []
        self.back(nums, temp)
        return self.res

    def back(self, nums, temp):
        if not nums:
            self.res.append(temp)
            return
        else:
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    # 当这次用的值和上次用的值相同时，直接跳过
                    continue
                self.back(nums[:i] + nums[i + 1:], temp + [nums[i]])  # 这种拼接方法是天然的标记，判断前一字符是否在循环里


class Solution:
    """
    https://leetcode-cn.com/problems/permutations-ii/solution/quan-pai-lie-ii-by-leetcode-solution/
    """

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        ans = []
        n = len(nums)
        visited = [0] * n

        def dfs():
            if len(ans) == n:
                res.append(ans[::])
            for i in range(n):
                if visited[i] or i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                ans.append(nums[i])
                visited[i] = 1
                dfs()
                ans.pop()
                visited[i] = 0

        dfs()
        return res
