class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        # 记录路径
        track = []
        self.backtrack(nums, track)
        return self.res

    def backtrack(self, nums, track):
        """
        路径：记录在 track 中

        选择列表：nums 中不存在于 track 的那些元素
        结束条件：nums 中的元素全都在 track 中出现
        """
        # 触发结束条件
        if len(track) == len(nums):
            self.res.append(list(track))
            return
        for one in nums:
            # 排除不合法的选择 选择列表：nums 中不存在于 track 的那些元素
            if one in track:
                continue
            # 做选择
            track.append(one)
            # 进入下一层决策树
            self.backtrack(nums, track)
            # 取消选择
            track.pop()

# result = []
#
#
# def backtrack(路径, 选择列表):
#     if 满足结束条件:
#         result.add(路径)
#         return
#
#     for 选择 in 选择列表:
#         做选择
#         backtrack(路径, 选择列表)
#         撤销选择

class Solution:
    """
    回溯算法
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
            return list(itertools.permutations(nums))


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


