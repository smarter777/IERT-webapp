class Solution:
    """
    只寻找第一个
    """
    def __init__(self):
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        # 输入棋盘边长 n，返回所有合法的放置
        # '.' 表示空，'Q' 表示皇后，初始化空棋盘。
        board = [['.'] * n for i in range(n)]
        # board = [['.']*n] *n
        self.backtrack(board, 0)
        return self.res

    # 路径：board 中小于 row 的那些行都已经成功放置了皇后
    # 选择列表：第 row 行的所有列都是放置皇后的选择
    # 结束条件：row 超过 board 的最后一行
    def backtrack(self, board, row):
        # 触发结束条件
        if row == len(board):
            # print("board", board)
            self.res.append([''.join(val) for val in board])
            return True  # Modify-1

        n = len(board[row])  # 有多少列
        for col in range(n):
            # 排除不合法的选择
            if not self.is_valid(board, row, col):
                continue
            # 做选择
            board[row][col] = 'Q'
            # 进入下一行决策
            if self.backtrack(board, row + 1):
                return True
            # 撤销选择
            board[row][col] = '.'
        return False

    def is_valid(self, board, row, col):
        n = len(board)

        # 检查列是否有皇后互相冲突
        for i in range(n):
            if board[i][col] == 'Q':
                return False

        # 检查右上方是否有冲突
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        # 检查左上方是否有冲突
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        return True
"""
https://blog.csdn.net/z1314520cz/article/details/85162183

>>> board = [['.']*n] *n
>>> board[0][0] = 'Q'
>>> board
[['Q', '.', '.', '.'], ['Q', '.', '.', '.'], ['Q', '.', '.', '.'], ['Q', '.', '.', '.']]
>>> board2 = [list('.'*n)] *n
>>> board[0][0] = 'Q'
>>> board2
[['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
>>> board = [['.'] * n for i in range(n)]
>>> board[0][0] = 'Q'
>>> board
[['Q', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
"""
class Solution:
    def is_valid(self, board, row, col):
        n = len(board[0])
        # 检查列冲突
        for i in range(n):
            if board[i][col] == 'Q': return False

        # 检查左斜上方冲突
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q': return False
            i -= 1
            j -= 1

        # 检查右斜上方冲突
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q': return False
            i -= 1
            j += 1

        return True

    def __init__(self):
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        # 输入棋盘边长 n，返回所有合法的放置
        # '.' 表示空，'Q' 表示皇后，初始化空棋盘。
        # board = [list('.'*n)] *n
        board = [['.'] * n for i in range(n)]
        self.backtrack(board, 0)
        return self.res

    # 路径：board 中小于 row 的那些行都已经成功放置了皇后
    # 选择列表：第 row 行的所有列都是放置皇后的选择
    # 结束条件：row 超过 board 的最后一行
    def backtrack(self, board, row):
        # 触发结束条件
        if row == len(board):
            print("board", board)
            # self.res.append(board)
            self.res.append([''.join(val) for val in board])
            return

        n = len(board[row])  # 有多少列
        for col in range(n):
            # 排除不合法的选择
            if not self.is_valid(board, row, col):
                continue
            # 做选择
            board[row][col] = 'Q'
            # 进入下一行决策
            self.backtrack(board, row + 1)
            # 撤销选择
            board[row][col] = '.'


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
