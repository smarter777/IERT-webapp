class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i, hashmap.get(target - num)]
            hashmap[num] = i  # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            partner = target - num
            if partner in nums[index + 1:]:
                partner_index = nums[index + 1:].index(partner) + index + 1
                if partner_index != -1:
                    return [index, partner_index]
