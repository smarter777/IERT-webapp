class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 按区间起点排序
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # print(interval)
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            # 末尾小于起点 [1,3] [4,5]
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # 重合
                # 否则的话，我们就可以与上一区间进行合并
                # 最后一个区间的末尾，等于interval的末尾 或
                merged[-1][1] = max(merged[-1][1], interval[1])
            # print("merged", merged)

        return merged