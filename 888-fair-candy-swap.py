class Solution:
    """
    通过优化b = set(B) 而不是直接 in B
    6660 ms -> 	548 ms
    """
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = sum(A) - sum(B)
        # print(diff)
        b = set(B)
        for i in range(len(A)):
            if (A[i] - diff/2) in b:
                return [A[i], A[i]-diff/2]


class Solution:
    """
    通过优化//  而不是直接 for one
    6660 ms -> 	368 ms
    """
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(A) - sum(B))//2
        # print(diff)
        b = set(B)
        for one in A:
            if (one - diff) in b:
                return [one, one-diff]