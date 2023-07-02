class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        end_index = 0
        for index, one in enumerate(nums):
            if target == one:
                return index
            if target > one:
                end_index = index+1
        return end_index


