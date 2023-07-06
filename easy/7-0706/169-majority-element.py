class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = Counter(nums)
        for num, freq in a.items():
            if freq > len(nums) / 2:
                return num


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for one in nums:
            if not hash_map.get(one):
                hash_map[one] = 1
            else:
                hash_map[one] += 1
        for num, freq in hash_map.items():
            if freq > len(nums) / 2:
                return num
