import heapq


class Solution1:
    def frequencySort(self, s: str) -> str:
        dic = {}
        res = ''
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        dic = sorted(dic.items(), key=lambda k: -k[1])
        for i in dic:
            for j in range(i[1]):
                res += i[0]
        return res


class Solution:
    def frequencySort(self, s: str) -> str:
        c_count = [0 for i in range(128)]
        for c in s:
            c_count[ord(c)] += 1
        res = ""
        index = 0
        while index < len(s):
            max_count = 0
            max_char = 0
            for i in range(len(c_count)):
                if c_count[i] > max_count:
                    max_count = c_count[i]
                    max_char = i
            # 置0
            c_count[max_char] = 0
            print(max_char, max_count)
            res = res + chr(max_char) * max_count
            index += 1
        return res


class Solution:
    def frequencySort(self, s: str) -> str:
        import collections
        _counter = collections.Counter(s)
        print(_counter)
        _heap = []
        for ele in _counter:
            heapq.heappush(_heap, (-_counter[ele], ele))
        print(_heap)
        s = ''
        for idx in range(len(_heap)):
            tmp = heapq.heappop(_heap)
            s += -tmp[0] * tmp[1]
        return s


if __name__ == '__main__':
    print(Solution().frequencySort("Aabb"))
