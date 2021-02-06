class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        na = len(A)
        nb = len(B)
        res = []
        while(i < na and j < nb):
            a = A[i]
            b = B[j]
            if(a[0]<=b[1] and a[1]>=b[0]):
                res.append([max(a[0], b[0]), min(a[1], b[1])])
            if(b[1]>a[1]):
                i += 1
            else:
                j += 1
        return res


class Solution:
    """
    作者：LeetCode
链接：https://leetcode-cn.com/problems/interval-list-intersections/solution/qu-jian-lie-biao-de-jiao-ji-by-leetcode/
    我们称 b 为区间 [a, b] 的末端点
    在两个数组给定的所有区间中，假设拥有最小末端点的区间是 A[0]。（为了不失一般性，该区间出现在数组 A 中)
    然后，在数组 B 的区间中， A[0] 只可能与数组 B 中的至多一个区间相交。
    （如果 B 中存在两个区间均与 A[0] 相交，那么它们将共同包含 A[0] 的末端点，但是 B 中的区间应该是不相交的，所以存在矛盾）

    如果 A[0] 拥有最小的末端点，那么它只可能与 B[0] 相交。然后我们就可以删除区间 A[0]，因为它不能与其他任何区间再相交了。
    如果 B[0] 拥有最小的末端点，那么它只可能与区间 A[0] 相交，然后我们就可以将 B[0] 删除，因为它无法再与其他区间相交了。

    我们用两个指针 i 与 j 来模拟完成删除 A[0] 或 B[0] 的操作。
    """
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            # 判断是否有交集的条件
            if lo <= hi:
                ans.append([lo, hi])

            # Remove the interval with the smallest endpoint
            # 哪个右区间元素较小，谁就被包含进去了，指针就向前移动一位
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans

