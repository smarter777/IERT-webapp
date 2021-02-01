class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        counts = 0
        intervals.sort()
        if len(intervals) == 0:
            return 0
        right = intervals[0][1]
        for val in intervals[1:]:
            if val[0] < right:
                right = min(right, val[1])
                counts += 1
            else:
                right = val[1]
        return counts


class Solution:
    """
    贪心算法
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        right = intervals[0][1]
        ans = 1

        for i in range(1, n):
            if intervals[i][0] >= right:
                ans += 1
                right = intervals[i][1]

        return n - ans


class Solution:
    """
    https://leetcode-cn.com/problems/non-overlapping-intervals/solution/wu-zhong-die-qu-jian-by-leetcode-solutio-cpsb/
    动态规划 6852
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()
        n = len(intervals)
        f = [1]

        for i in range(1, n):
            f.append(max((f[j] for j in range(i) if intervals[j][1] <= intervals[i][0]), default=0) + 1)

        return n - max(f)


class Solution:
    """
    没脑子一通乱写，没有通过
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals)
        print(intervals)
        min_start = intervals[0][0]
        min_end = intervals[0][1]
        conut = 0
        for one in intervals[1:]:
            if one[0] == min_start and one[1] >= min_end:
                print(one)
                conut += 1
            elif one[0] > min_start and one[0] < min_end:
                print(one)
                # [1, 11]  [2, 12]
                conut += 1
            elif one[0] > min_end:
                min_start = one[0]
                min_end = one[1]
        return conut
