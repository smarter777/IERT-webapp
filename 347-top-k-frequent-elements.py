class Solution:
    def topKFrequent(self, nums, k: int):
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        return sorted(dic, key=lambda x: dic[x])[::-1][:k]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = dict(collections.Counter(nums))
        res = []
        sorted_items = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            res.append(sorted_items[i][0])
        return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq as hq
        freq = {}
        heap = []
        res = []
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for num, count in freq.items():
            if len(heap) < k:
                hq.heappush(heap, (count, num))
            else:
                if heap[0][0] < count:
                    hq.heapreplace(heap, (count, num))
        while heap:
            res.append(hq.heappop(heap)[1])
        return res
