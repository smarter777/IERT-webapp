# https://leetcode-cn.com/problems/triangle/solution/san-chong-jie-fa-duo-tu-xiang-jie-120-san-jiao-xin/
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]


'''设三角形每层数组为curLevel，设每层最小路径和列表dpdp。
dpdp初始化为triangle最底层一列数据。
每层递推公式：dp[i] = triangle[i]+min(dp[i],dp[i+1])
算法步骤：
利用一维数组记录每层每个位置的最小路径和，初始化dp = triangle[-1];
从三角形倒数第二层开始遍历：
遍历该层每个位置：
对每个位置依据公式dp[i] = triangle[i]+min(dp[i],dp[i+1])求出该位置最小路径和
返回dp[0]

'''


class Solution(object):
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        n = len(triangle)
        m = len(triangle[-1])
        # 申请的dp数组为最长列+1
        dp = [0 for _ in range(m + 1)]
        for i in range(n - 1, -1, -1):
            # 从左到右的方式计算
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        # dp数组的第一个元素即为最终结果
        return dp[0]
