class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):
            record = {}  # record中存储 点i 到所有其他点的距离出现的频次
            for j in range(len(points)):
                if j != i:
                    # 计算距离时不进行开根运算, 以保证精度
                    distance = self.cal_distance(points[i], points[j])
                    if distance not in record:
                        record[distance] = 1
                    else:
                        record[distance] += 1
            for key, value in record.items():
                res += value * (value - 1)
        return res

    def cal_distance(self, a, b):
        return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        for x1,y1 in points:
            hash = {}
            for x2,y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                dx = x1-x2
                dy = y1-y2
                d = dx * dx + dy * dy
                if d not in hash:
                    hash[d] = 1
                else:
                    count += hash[d]
                    hash[d] += 1
        return count*2