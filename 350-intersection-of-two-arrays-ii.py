class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = set(nums1) & set(nums2)
        l = []
        for i in inter:
            l += [i] * min(nums1.count(i), nums2.count(i))
        return l

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        record_map = {}
        for one in nums1:
            if one not in record_map:
                record_map[one] = 1
            else:
                record_map[one] += 1
        res = []
        # print(record_map)
        for two in nums2:
            if two in record_map and record_map[two] > 0:
                res.append(two)
                record_map[two] -= 1
                """
                [4,9,5]
                [9,4,9,8,4]
                """
        return res


class Solution:
    # 48 ms
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        if not nums1 or not nums2 : return
        counter_1 = Counter(nums1)
        counter_2 = Counter(nums2)
        num = counter_1 & counter_2
        return num.elements()