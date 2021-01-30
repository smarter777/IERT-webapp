class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = []
        for i in range(n):
            for j in range(i + 1):
                if (s[i] == s[j]) and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True

        def backstack(tmp, idx=0):
            if idx == n:
                res.append(tmp)
            for i in range(idx, n):
                if dp[idx][i]:
                    backstack(tmp + [s[idx:i + 1]], i + 1)

        backstack([])
        return res


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def helper(s, tmp):
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tmp + [s[:i]])

        helper(s, [])
        return res