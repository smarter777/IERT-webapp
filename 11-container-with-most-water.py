from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            # min_height = height[r] if height[l] > height[r] else height[l]
            min_height = min(height[r], height[l])
            cur_area = min_height * (r - l)

            if cur_area > max_area:
                max_area = cur_area
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return max_area
