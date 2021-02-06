import collections
from typing import List


class Solution:

    # 将s[j] 向上拨动一次
    def plus_one(self, s, j):
        s = list(s)
        if s[j] == '9':
            s[j] = '0'
        else:
            s[j] = str(int(s[j]) + 1)
        return "".join(s)

    # 将s[j] 向下拨动一次
    def minus_one(self, s, j):
        s = list(s)
        if s[j] == '0':
            s[j] = '9'
        else:
            s[j] = str(int(s[j]) - 1)
        return "".join(s)

    def openLock(self, deadends: List[str], target: str) -> int:
        # 记录需要跳过的死亡密码
        deads = set(deadends)
        # 用集合不用队列，可以快速判断元素是否存在
        q1 = set()
        q2 = set()
        visited = set()  # 记录已经穷举过的密码，防止走回头路

        # 从起点开始启动广度优先搜索
        step = 0
        q1.add("0000")
        q2.add(target)

        while q1 and q2:
            """
            if (q1.size() > q2.size()) {
                // 交换 q1 和 q2
                temp = q1;
                q1 = q2;
                q2 = temp;
            }
            BFS 的逻辑，队列（集合）中的元素越多，扩散之后新的队列（集合）中的元素就越多；
            在双向 BFS 算法中，如果我们每次都选择一个较小的集合进行扩散，
            那么占用的空间增长速度就会慢一些，效率就会高一些。
            """
            # 哈希集合在遍历的过程中不能修改，用 temp 存储扩散结果
            temp = set()

            # 将 q1 中的所有节点向周围扩散
            for cur in q1:

                # 判断是否到达终点
                if cur in deads:
                    continue
                if cur in q2:
                    return step
                visited.add(cur)

                # 将一个节点的未遍历相邻节点加入队列
                for j in range(4):
                    up = self.plus_one(cur, j)
                    if not (up in visited):
                        temp.add(up)
                    down = self.minus_one(cur, j)
                    if not (down in visited):
                        temp.add(down)

            # 这里添加步数
            step += 1

            # temp 相当于q1
            # 这里交换 q1 q2，下一轮 while 就是扩散 q2
            q1 = q2
            q2 = temp

        # 如果穷举完都没找到目标密码，那就是找不到了
        return -1


class Solution(object):
    """
    https://leetcode-cn.com/problems/open-the-lock/solution/da-kai-zhuan-pan-suo-by-leetcode/
    广度优先搜索
    """

    def openLock(self, deadends, target):
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i + 1:]

        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in dead: continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth + 1))
        return -1


class Solution:
    # 将s[j] 向上拨动一次
    def plus_one(self, s, j):
        s = list(s)
        if s[j] == '9':
            s[j] = '0'
        else:
            s[j] = str(int(s[j]) + 1)
        return "".join(s)

    # 将s[j] 向下拨动一次
    def minus_one(self, s, j):
        s = list(s)
        if s[j] == '0':
            s[j] = '9'
        else:
            s[j] = str(int(s[j]) - 1)
        return "".join(s)

    def bfs(self, target):
        q = collections.deque()
        q.append("0000")

        while q:
            print(q)
            sz = len(q)
            # 将当前队列中的所有节点向周围扩散
            for i in range(sz):
                cur = q.popleft()
                # 判断是否到达终点

                # 将一个节点的相邻节点加入队列
                for j in range(4):
                    up = self.plus_one(cur, j)
                    down = self.minus_one(cur, j)
                    q.append(up)
                    q.append(down)

            # 这里增加步数
        return

    def openLock(self, deadends: List[str], target: str) -> int:
        self.bfs(1)
