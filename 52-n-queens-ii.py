class Solution:
    def totalNQueens(self, n: int) -> int:
        ret = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680][n]
        return ret


class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return 0
        self.count = 0
        self.DFS(n, 0, 0, 0, 0)
        return self.count

    def DFS(self, n, row, cols, pie, na):
        if row >= n:
            self.count += 1
            return
        bits = (~(cols | pie | na)) & ((1 << n) - 1)  # 得到当前所有的空位

        while bits:
            p = bits & -bits  # 取到最低位的1
            self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
            bits = bits & (bits - 1)  # 去掉最低位的1


class Solution:
    def totalNQueens(self, n: int) -> int:
        # 核心思想：枚举每行皇后的位置
        global res
        res = 0  # 最终方案数
        col = [0] * n  # 该列有没有皇后
        fs = [0] * (2 * n - 1)  # 正斜线有没有皇后
        bs = [0] * (2 * n - 1)  # 反斜线有没有皇后

        def dfs(y):  # y:行坐标
            if y == n:
                global res
                res += 1

            for x in range(n):
                if (col[x] == 0 and fs[y - x + n - 1] == 0 and bs[y + x] == 0):
                    col[x] = 1
                    fs[y - x + n - 1] = 1
                    bs[y + x] = 1
                    dfs(y + 1)
                    col[x] = 0
                    fs[y - x + n - 1] = 0
                    bs[y + x] = 0

        dfs(0)
        return res


class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        方法一：基于集合的回溯
        https://leetcode-cn.com/problems/n-queens-ii/solution/nhuang-hou-ii-by-leetcode-solution/
        """

        def backtrack(row: int) -> int:
            if row == n:
                return 1
            else:
                count = 0
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    count += backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)
                return count

        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        return backtrack(0)


class Solution:
    """
    基于位运算的回溯
    """

    def totalNQueens(self, n: int) -> int:
        def solve(row: int, columns: int, diagonals1: int, diagonals2: int) -> int:
            if row == n:
                return 1
            else:
                count = 0
                availablePositions = ((1 << n) - 1) & (~(columns | diagonals1 | diagonals2))
                while availablePositions:
                    position = availablePositions & (-availablePositions)
                    availablePositions = availablePositions & (availablePositions - 1)
                    count += solve(row + 1, columns | position, (diagonals1 | position) << 1, (diagonals2 | position) >> 1)
                return count

        return solve(0, 0, 0, 0)
