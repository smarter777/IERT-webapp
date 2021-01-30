class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 回溯，以[1, 2, 3]为例
        # 1.加入空数组[]
        # 2.枚举长度为1的子集
        # 3.递归进入枚举长度为2的子集
        # 4.递归进入枚举长度为3的子集
        # 5.tmp + [nums[i]]不对tmp本身做修改，自动完成选择与释放选择
        res = []

        def dfs(index, tmp):
            res.append(tmp)
            for i in range(index, len(nums)):
                dfs(i + 1, tmp + [nums[i]])

        dfs(0, [])
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        https://leetcode-cn.com/problems/subsets/solution/hui-su-python-dai-ma-by-liweiwei1419/
        这个题蛮有意思的，可以直接从后遍历，遇到一个数就把所有子集加上该数组成新的子集，遍历完毕即是所有子集
        """
        size = len(nums)
        if size == 0:
            return []

        res = []
        self.__dfs(nums, 0, [], res)
        return res

    def __dfs(self, nums, start, path, res):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            # 因为 nums 不包含重复元素，并且每一个元素只能使用一次
            # 所以下一次搜索从 i + 1 开始
            self.__dfs(nums, i + 1, path, res)
            path.pop()
