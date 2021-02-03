import heapq
import collections


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k==1:
            return nums
        m = collections.defaultdict(int)
        if k % 2:
            l = k // 2
            r = k // 2 + 1
            diff = 1
        else:
            l = r = k // 2
            diff = 0
        lmi = []
        rma = []
        for i in range(k):
            heapq.heappush(rma, nums[i])  # 小顶堆存右半边
        for i in range(k // 2):
            heapq.heappush(lmi, -heapq.heappop(rma))  # 大顶堆存左半边
        ans = [rma[0] if r > l else (rma[0] - lmi[0]) / 2]
        for i in range(k, len(nums)):
            m[nums[i - k]] += 1
            l += 1  # 每次都加一个数加到右半组，再从右半组弹一个数到左半组，相当于给左半组加了1个
            if nums[i - k] <= -lmi[0]:
                l -= 1
            else:
                r -= 1
            heapq.heappush(lmi, -heapq.heappushpop(rma, nums[i]))
            if r - l > diff:
                heapq.heappush(lmi, -heapq.heappop(rma))
                l += 1
            elif r - l < diff:
                heapq.heappush(rma, -heapq.heappop(lmi))
                r += 1
                l -= 1
            while m[-lmi[0]] > 0:
                num = -heapq.heappop(lmi)
                m[num] -= 1
            while m[rma[0]] > 0:
                num = heapq.heappop(rma)
                m[num] -= 1
            ans.append(rma[0] if r > l else (rma[0] - lmi[0]) / 2)
        return ans


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        i,ret = 0, []
        while i+k <= len(nums):
            cur_win_mid = sorted(nums[i:i+k])[(k-1)//2] if k % 2 == 1 else (sorted(nums[i:i+k])[k//2] + sorted(nums[i:i+k])[k//2-1]) / 2
            ret.append(cur_win_mid)
            i += 1
        return ret




class DualHeap:
    def __init__(self, k: int):
        # 大根堆，维护较小的一半元素，注意 python 没有大根堆，需要将所有元素取相反数并使用小根堆
        self.small = list()
        # 小根堆，维护较大的一半元素
        self.large = list()
        # 哈希表，记录「延迟删除」的元素，key 为元素，value 为需要删除的次数
        self.delayed = collections.Counter()

        self.k = k
        # small 和 large 当前包含的元素个数，需要扣除被「延迟删除」的元素
        self.smallSize = 0
        self.largeSize = 0

    # 不断地弹出 heap 的堆顶元素，并且更新哈希表
    def prune(self, heap: List[int]):
        while heap:
            num = heap[0]
            if heap is self.small:
                num = -num
            if num in self.delayed:
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    self.delayed.pop(num)
                heapq.heappop(heap)
            else:
                break

    # 调整 small 和 large 中的元素个数，使得二者的元素个数满足要求
    def makeBalance(self):
        if self.smallSize > self.largeSize + 1:
            # small 比 large 元素多 2 个
            heapq.heappush(self.large, -self.small[0])
            heapq.heappop(self.small)
            self.smallSize -= 1
            self.largeSize += 1
            # small 堆顶元素被移除，需要进行 prune
            self.prune(self.small)
        elif self.smallSize < self.largeSize:
            # large 比 small 元素多 1 个
            heapq.heappush(self.small, -self.large[0])
            heapq.heappop(self.large)
            self.smallSize += 1
            self.largeSize -= 1
            # large 堆顶元素被移除，需要进行 prune
            self.prune(self.large)

    def insert(self, num: int):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.smallSize += 1
        else:
            heapq.heappush(self.large, num)
            self.largeSize += 1
        self.makeBalance()

    def erase(self, num: int):
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.smallSize -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.largeSize -= 1
            if num == self.large[0]:
                self.prune(self.large)
        self.makeBalance()

    def getMedian(self) -> float:
        return float(-self.small[0]) if self.k % 2 == 1 else (-self.small[0] + self.large[0]) / 2


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        dh = DualHeap(k)
        for num in nums[:k]:
            dh.insert(num)

        ans = [dh.getMedian()]
        for i in range(k, len(nums)):
            dh.insert(nums[i])
            dh.erase(nums[i - k])
            ans.append(dh.getMedian())

        return ans

