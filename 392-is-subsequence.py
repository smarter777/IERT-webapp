class Solution:
    """
    二分法
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        from collections import defaultdict
        import bisect
        lookup = defaultdict(list)
        for idx, val in enumerate(t):
            lookup[val].append(idx)
        # print(lookup)
        loc = -1
        for a in s:
            j = bisect.bisect_left(lookup[a], loc + 1)
            if j >= len(lookup[a]): return False
            loc = lookup[a][j]
        return True

class Solution:
    """
    双指针法
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            # print(i, j)
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        # for c in s:
        #     """
        #     a True
        #     c True
        #     b False
        #     """
        #     print(c , c in t)
        return all(c in t for c in s)


class Solution:
    """
    库函数
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        loc = -1
        for a in s:
            loc = t.find(a, loc + 1)
            if loc == -1:
                return False
        return True


class Solution:
    """
    生成迭代器
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(c in t for c in s)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n
