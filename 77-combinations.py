class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))


class Solution:
    """
    排列组合的性质C(m,n)=C(m-1,n)+C(m-1,n-1)
    """

    def combine(self, n, k):
        if k > n or k == 0:
            return []
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        if k == n:
            return [[i for i in range(1, n + 1)]]

        answer = self.combine(n - 1, k)
        for item in self.combine(n - 1, k - 1):
            item.append(n)
            answer.append(item)

        return answer


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def dfs(n, k, path, start):
            if len(path) == k:
                ans.append(path[:])
                return
            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                dfs(n, k, path, i + 1)
                path.pop()

        dfs(n, k, [], 1)
        return ans

