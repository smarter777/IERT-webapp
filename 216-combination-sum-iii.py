class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return list(filter(lambda l: sum(l) == n, itertools.combinations(range(1, 10), k)))


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        from itertools import combinations
        return [list(l) for l in combinations(range(1, 10), k) if sum(l) == n]


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtrack(cur, prev, tmp):
            if tmp == k and sum(cur) == n:
                ans.append(cur)
                return
            for j in range(prev, 10):
                backtrack(cur=cur + [j], prev=j + 1, tmp=tmp + 1)

        backtrack(cur=[], prev=1, tmp=0)
        return ans
