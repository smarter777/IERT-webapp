class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        re_min = 0  # 存储当前最小的差值

        for i in range(n):
            low = i + 1
            high = n - 1
            while low < high:
                three_sum = nums[i] + nums[low] + nums[high]
                x = target - three_sum  # 当前三数的差值
                if re_min == 0:
                    re_min = abs(x)
                    sum_min = three_sum  # sum_min为当前最接近的和

                if abs(x) < re_min:
                    re_min = abs(x)
                    sum_min = three_sum

                if three_sum == target:
                    return target
                elif three_sum < target:
                    low += 1
                else:
                    high -= 1

        return sum_min