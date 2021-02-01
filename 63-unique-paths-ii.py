class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        nrow = len(obstacleGrid)
        ncol = len(obstacleGrid[0])

        if nrow <= 1 or ncol <= 1:
            for i in range(nrow):
                for j in range(ncol):
                    if obstacleGrid[i][j] == 1:
                        return 0
            else:
                return 1

        if obstacleGrid[0][0] == 1:
            return 0

        path = [[0] * ncol for i in range(nrow)]

        # 第一行只有一种走法，且如果障碍在第一行，则障碍后面的值都不可达到，走法为0
        flag = False
        for i in range(ncol):
            # 障碍还没出现
            if not flag and obstacleGrid[0][i] != 1:
                path[0][i] = 1
            else:  # 障碍出现
                path[0][i] = 0
                flag = True

        # 第一列也只有一种走法，且如果障碍在第一列，则障碍后面的值都不可达到，走法为0
        flag = False
        for i in range(nrow):
            # 障碍还没出现
            if not flag and obstacleGrid[i][0] != 1:
                path[i][0] = 1
            else:  # 障碍出现
                path[i][0] = 0
                flag = True

        for row in range(1, nrow):
            for col in range(1, ncol):
                if obstacleGrid[row][col] != 1:
                    path[row][col] = path[row - 1][col] + path[row][col - 1]
                else:
                    path[row][col] = 0

        return path[nrow - 1][ncol - 1]


class Solution:
    """
    https://leetcode-cn.com/problems/unique-paths-ii/solution/python-ji-chu-xie-fa-fu-shang-yi-chu-shi-hua-da-ke/

    https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly
    """

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # dp = [[0]*n]*m  注意这样申请矩阵有问题, 每一行[0]*n 联动变, 像是一个dp存地址一样
        dp = [[0 for j in range(n)] for i in range(m)]

        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        for j in range(1, n):
            dp[0][j] = 0 if obstacleGrid[0][j] else dp[0][j - 1]
        for i in range(1, m):
            dp[i][0] = 0 if obstacleGrid[i][0] else dp[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = 0 if obstacleGrid[i][j] else dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
