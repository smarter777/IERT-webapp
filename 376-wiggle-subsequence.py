class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        dp = [[1,1] for i in range(len(nums))]
        # dp[i][0] 表示 在第i个位置 是上升状态的 最长摆动序列长度
        # dp[i][1] 表示 在第i个位置 是下降状态的 最长摆动序列长度
        ans = 1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i][0] = max(dp[j][1]+1,dp[i][0])
                elif nums[i]<nums[j]:
                    dp[i][1] = max(dp[i][1],dp[j][0]+1)
            ans = max(dp[i][0],dp[i][1],ans)
        return ans

class Solution:
    """
    贪心
    """

    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        # 1. 长度为1的都是摆动序列
        if n < 2:
            return n

        # 2. 初始化
        prevdiff = nums[1] - nums[0]  # 记录相邻三个元素 x y z(x 和 y 的差是正还是负)
        ret = (2 if prevdiff != 0 else 1)  # 前两个元素是否有重复
        # 3. 贪心遍历数组:加入一个新元素
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]  # 记录相邻三个元素 x y z(y 和 z 的差是正还是负)
            if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
                # 判断当前序列的上升下降趋势
                ret += 1  # 如果出现了「峰」或「谷」，答案加一
                prevdiff = diff  # 更新当前序列的上升下降趋势

        return ret


