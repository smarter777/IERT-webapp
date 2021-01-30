"""
https://www.bilibili.com/video/BV1754y1v7jt
"""


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        go_Pacific = self.can_go_Pacific(matrix)
        go_Atlantic = self.can_go_Atlantic(matrix)
        return list(go_Pacific & go_Atlantic)

    def can_go_Pacific(self, grid):
        ## BFS
        q = []
        m, n = len(grid), len(grid[0])
        for j in range(n):
            q.append((0, j))
        for i in range(1, m):
            q.append((i, 0))
        visited = set(q)
        while q:
            newq = []
            for i, j in q:
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= i + di < m and 0 <= j + dj < n and (i + di, j + dj) not in visited and grid[i + di][j + dj] >= grid[i][j]:
                        visited.add((i + di, j + dj))
                        newq.append((i + di, j + dj))
            q = newq
        return visited

    def can_go_Atlantic(self, grid):
        q = []
        m, n = len(grid), len(grid[0])
        for j in range(n):
            q.append((m - 1, j))
        for i in range(m - 1):
            q.append((i, n - 1))
        visited = set(q)
        while q:
            newq = []
            for i, j in q:
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= i + di < m and 0 <= j + dj < n and (i + di, j + dj) not in visited and grid[i + di][j + dj] >= grid[i][j]:
                        visited.add((i + di, j + dj))
                        newq.append((i + di, j + dj))
            q = newq
        return visited

class Solution:
    def __init__(self):
        self.result_all = None
        # 分别表示上右下左
        self.directs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.m = 0
        self.n = 0
        # 表示能流到太平洋
        self.po = None
        # 表示能流到大西洋
        self.ao = None
        self.visited = None

    def pacificAtlantic(self, matrix):
        # 初始化一些东西
        self.result_all = []
        self.m = len(matrix)
        if self.m == 0:
            return self.result_all
        self.n = len(matrix[0])
        self.ao = [[0] * self.n for _ in range(self.m)]
        self.po = [[0] * self.n for _ in range(self.m)]
        self.visited = [[0] * self.n for _ in range(self.m)]

        # 本题顺着流不太好做，我们用逆流的方式来思考
        # 从上面的太平洋逆流
        for i in range(0, 1):
            for j in range(self.n):
                self.dfs(matrix, i, j, True)
        # 从左边的太平洋逆流
        self.visited = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(0, 1):
                self.dfs(matrix, i, j, True)
        # 下面的大西洋
        self.visited = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m - 1, self.m):
            for j in range(self.n):
                self.dfs(matrix, i, j, False)
        # 右边的大西洋
        self.visited = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n - 1, self.n):
                self.dfs(matrix, i, j, False)

        for i in range(self.m):
            for j in range(self.n):
                if self.po[i][j] == 1 and self.ao[i][j] == 1:
                    self.result_all.append((i, j))
        return self.result_all

    def dfs(self, matrix, x, y, flag):
        if self.visited[x][y] == 1:
            return
        self.visited[x][y] = 1
        if flag:
            # 表示是太平洋
            self.po[x][y] = 1
        else:
            # 表示是大西洋
            self.ao[x][y] = 1

        for i in range(4):
            newx = x + self.directs[i][0]
            newy = y + self.directs[i][1]
            if not self.in_area(newx, newy):
                continue
            if matrix[x][y] > matrix[newx][newy]:
                continue
            self.dfs(matrix, newx, newy, flag)
        return

    def in_area(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n

