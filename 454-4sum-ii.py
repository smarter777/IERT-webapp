class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count = 0
        ab_map = dict()

        for a in A:
            for b in B:
                ab_map[a + b] = ab_map.get(a + b, 0) + 1

        for c in C:
            for d in D:
                s = -(c + d)
                if s in ab_map:
                    count += ab_map[s]

        return count


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ans = 0
        counter_a = Counter(A)
        counter_b = Counter(B)
        counter_c = Counter(C)
        counter_d = Counter(D)
        union_a_b = dict()
        for num_a, count_a in counter_a.items():
            for num_b, count_b in counter_b.items():
                tmp_sum = num_a + num_b
                union_a_b[tmp_sum] = union_a_b.get(tmp_sum, 0) + (count_a *
                                                                  count_b)

        for num_c, count_c in counter_c.items():
            for num_d, count_d in counter_d.items():
                tmp_sum = num_c + num_d
                if 0 - tmp_sum in union_a_b:
                    tmp_comb = count_c * count_d
                    ans += tmp_comb * union_a_b[0-tmp_sum]

        return ans
