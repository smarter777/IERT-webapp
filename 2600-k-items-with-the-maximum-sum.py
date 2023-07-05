class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # 贪心，取尽量多的1和0，取最少的-1
        if k <= numOnes:
            return k
        elif k <= numOnes + numZeros:
            return numOnes
        else:
            return numOnes - (k - numOnes - numZeros)


class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes >= k:
            return k
        elif numOnes < k < numOnes + numZeros:
            return numOnes
        else:
            # 拿走所有的0和1，剩下的-1数量减去
            return numOnes - (k - numOnes - numZeros)
