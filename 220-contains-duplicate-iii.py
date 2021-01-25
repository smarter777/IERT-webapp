from sortedcontainers import SortedSet


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        sorted_set = SortedSet()

        for i in range(len(nums)):
            num = nums[i]

            # find the successor of current element
            if sorted_set and sorted_set.bisect_left(num) < len(sorted_set):
                if sorted_set[sorted_set.bisect_left(num)] <= num + t:
                    return True

            # find the predecessor of current element
            if sorted_set and sorted_set.bisect_left(num) != 0:
                if num <= sorted_set[sorted_set.bisect_left(num) - 1] + t:
                    return True

            sorted_set.add(num)
            if len(sorted_set) > k:
                sorted_set.remove(nums[i - k])

        return False


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # 1. 遍历：在k的索引范围内遍历“t”的条件是否满足

        # 2. 建立hash桶（桶排序）
        # 该题与存在重复元素II的差异性主要体现在建立hash table
        # 存在重复元素II
        # hash_table = {}
        # for i in range(len(nums)):
        #     if nums[i] not in hash_table:
        #         hash_table[nums[i]] = [i]
        #     else:#in
        #         if abs(i - hash_table[nums[i]][-1]) > k:
        #             hash_table[nums[i]].pop()
        #             hash_table[nums[i]].append(i)

        #         else:# <= k
        #             return True
        # return False

        # 存在重复元素III
        hash_bucket = dict()
        if t < 0:
            return False
        for i in range(len(nums)):
            bucket_size = t + 1
            bucket_index = nums[i] // bucket_size
            if bucket_index in hash_bucket:
                return True
            if bucket_index - 1 in hash_bucket and abs(nums[i] - hash_bucket[bucket_index - 1]) <= t:
                return True
            if bucket_index + 1 in hash_bucket and abs(nums[i] - hash_bucket[bucket_index + 1]) <= t:
                return True

            # 不在hash_bucket中
            hash_bucket[bucket_index] = nums[i]

            if i >= k:
                hash_bucket.pop(nums[i - k] // bucket_size)
        return False
