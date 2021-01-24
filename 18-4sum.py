class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        # 数组为null 或数组长度小于3，返回[]
        if not nums or n < 4:
            return []
        nums.sort()  # 排序
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 对于重复元素：跳过，避免出现重复解
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue  # 对于重复元素：跳过，避免出现重复解
                L = j + 1
                R = n - 1
                while L < R:
                    sum_total = nums[i] + nums[j] + nums[L] + nums[R]
                    if sum_total == target:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        # 执行循环，判断左界和右界是否和下一位置重复，
                        # 去除重复解。并同时将 L,R 移到下一位置，寻找新的解
                        while L < R and nums[L] == nums[L + 1]:
                            L = L + 1
                        while L < R and nums[R] == nums[R - 1]:
                            R = R - 1
                        L = L + 1
                        R = R - 1
                    elif sum_total > target:
                        R = R - 1
                    else:
                        L = L + 1
        return res

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        dic = {}
        nums.sort()
        MIN,MAX = nums[0],nums[-1]
        n  = 4
        for i in range(len(nums)-1):
            if nums[i] + (n-1)*MAX < target:
                continue
            if nums[i]*(n-2) + (n-2) *MIN > target:
                break
            for j in range(i+1,len(nums)):
                num = nums[i]+nums[j]
                if not(num + (n-2)*MAX < target or num + (n-2)*MIN > target):
                    dic.setdefault(num,[]).append((i,j))

        result = set()
        keys = [num for num in dic if (n-2)*num <= target and target-num in dic]
        for num in keys:
            for i,j in dic[num]:
                for x,y in dic[target - num]:
                    if j < x:
                        result.add((nums[i],nums[j],nums[x],nums[y]))
        return [list(t) for t in result]


