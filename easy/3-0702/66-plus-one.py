class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for index, one in enumerate(digits[::-1]):
            unit = 10 ** index
            num += one * unit
        return [int(one) for one in list(str(num+1))]