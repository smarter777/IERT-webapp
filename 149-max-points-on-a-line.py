class Solution:
    def maxPoints(self, points):
        res = 0
        if not points:
            return res
        for i in range(len(points)):
            dic = {}
            same = 0
            curMax = 0
            for j in range(i+1, len(points)):
                if points[i] == points[j]:
                    same += 1
                    continue
                if (points[i][0] - points[j][0]) == 0:
                    rate = float('inf')
                else:
                    rate = (points[i][1] - points[j][1]) * 1000 / (points[i][0] - points[j][0]) * 1000
                dic[rate] = dic.get(rate, 0) + 1
                curMax = max(curMax, dic[rate])
            res = max(res, curMax+same+1)
        return res


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0

        points = sorted(points)

        res = 1
        for i in range(len(points) - 1):
            dicts = {}
            basic_num = 1
            for j in range(i + 1, len(points)):
                if points[j] == points[i]:
                    basic_num += 1
                else:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    if x2 - x1 == 0:
                        xielv = 'c'
                    else:
                        xielv = (y2 - y1) * 1000 / (x2 - x1)
                    dicts[xielv] = dicts.get(xielv, 0) + 1
            if len(dicts) == 0:
                if res < basic_num:
                    res = basic_num
            else:
                for val in dicts.values():
                    if res < val + basic_num:
                        res = val + basic_num
        return res

