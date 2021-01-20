from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0  # length表示的是删除重复元素后新序列的长度，同时也表示新元素进入新序列的索引；
        for i in range(len(nums)):
            # i就是循环变量，用于遍历整个旧序列；
            if length < 2 or nums[i] != nums[length - 2]:
                """
                if (length < 2) 
                nums[length++] = nums[i]
                如果新序列的长度小于2（即新序列中不会存在两个相同的元素，
                这时候i位置所在元素不会和新序列中的元素相同），
                直接将新元素加入到新序列中，并更新新序列的长度；
                """

                """
                if (nums[i] != nums[length-2])
                nums[len++] = nums[i]
                如果新元素加入后不会和前两个元素构成3个相同的元素
               （nums[length-2]就是直接取新序列中倒数第二个元素，[1,1] <- 1 [1,2] <- 1
                可是只比较了新元素和倒数第二个啊 “121” 就不是三连。。已排序的数组，不会再出现1
                如果该元素和新元素相同，说明加入后会构成3个相同的元素，显然是不符合题意的）
                就将新元素加入到新序列中，并更新新序列的长度；
                """
                nums[length] = nums[i]
                length += 1
        return length


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1  # [0, k)中存储出现2次及以下的元素
        count = 1  # 表示元素出现的次数
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                if count < 2:
                    nums[k] = nums[i]
                    k += 1
                count += 1
            else:
                nums[k] = nums[i]
                k += 1
                count = 1
        return k
