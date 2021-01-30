class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        ans = []
        for b in board:
            ans += b
        need = Counter(word)
        ans = Counter(ans)
        for k, v in need.items():
            if v > ans[k]:
                return False

        def back(i, j, word):
            if len(word) == 0:
                return True
            if not (0 <= i < m and 0 <= j < n and board[i][j] != '#' and board[i][j] == word[0]):
                return False

            temp, board[i][j] = board[i][j], '#'
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if back(x, y, word[1:]):
                    return True
            board[i][j] = temp

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    # temp, board[i][j] = board[i][j], '#'
                    if back(i, j, word):
                        return True
                    # board[i][j] = temp
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        cb = collections.Counter([i for inner in board for i in inner])
        cw = collections.Counter(word)
        if cb & cw != cw: return False

        m, n = len(board), len(board[0])
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右四个方向

        def dfs(i, j, k, visited):
            if k > len(word) - 1: return  # 判断是否已经到了单词的最后一个字符了
            if board[i][j] == word[k]:  # 如果当前的字符与单词的第k个字符相等的话，继续
                if k == len(word) - 1:  # 如果已经到了最后一个字符，返回正确
                    return True
                else:
                    visited.add((i, j))  # 继续下一步移动之前，先将当前位置加入到path中去。因为下一步无论走哪个方向，当前位置都是path上的一个点
                    for x, y in direction:  # 用x，y表示移动的方向，接下来再表示下一个点的位置，比直接用i+x, j+y方便一些
                        x, y = i + x, j + y
                        if x < 0 or x > m - 1 or y < 0 or y > n - 1 or (x, y) in visited:  # 如果越界了，或者已经访问过了，直接跳过
                            continue
                        if dfs(x, y, k + 1, visited):
                            return True
                    visited.remove((i, j))  # 当将当前位置所有的子路径都走完之后，表明当前位置行不通，需要更换路径。因此，当前位置需要从当前路径中清除

        for i in range(m):
            for j in range(n):
                visited = set()
                if dfs(i, j, 0, visited):
                    return True
        return False


class Solution:
    """
    深度优先搜索
    https://leetcode-cn.com/problems/word-search/solution/dan-ci-sou-suo-by-leetcode-solution/
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break

            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True

        return False
