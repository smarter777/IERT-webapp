class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 建立一个大小不超过k的散列表或者说窗口
        k_windows = set()
        for i in range(len(nums)):
            # 如果当前元素在窗口中存在了，说明满足条件了，直接返回true
            if nums[i] in k_windows:
                return True
            # 否则将该元素添加到窗口中
            k_windows.add(nums[i])
            # 检查窗口的大小是否超过了k，如果超过了k,意味着
            #   1.当前窗口一个重复元素都没有，因为如果有的话，肯定就返回true了
            #   2.当前窗口的第一个元素也就是nums[i-k]没有用了，
            #     因为找不到它的在以k为大小的窗口内的重复元素，所以可以把它删除了。
            if len(k_windows) > k:
                k_windows.remove(nums[i - k])
        return False


"""
用一个hash table存信息
key是当前元素 value是对应的index
初始为空
遍历数组 如果当前元素在这个hash table 并且当前下标的差值<=k 就返回True
默认返回False
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        temp_dict = {}

        for i in range(len(nums)):
            if nums[i] in temp_dict and i - temp_dict[nums[i]] <= k:
                return True
            temp_dict[nums[i]] = i
        return False