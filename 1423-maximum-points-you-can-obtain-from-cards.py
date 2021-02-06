class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        维护一个len-k的窗口，保证窗口里面和最小，然后剩余的k个数的和就是最大
        """
        len_list = len(cardPoints)
        sum_total = 0
        for card in cardPoints:
            sum_total += card
        min_value = float('inf')
        temp = 0
        length_min = len_list - k
        for i in range(len_list):
            temp += cardPoints[i]
            if i >= length_min:
                temp -= cardPoints[i-length_min]
            if i >= length_min - 1:
                min_value = min(min_value, temp)
        return sum_total - min_value


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_id=0
        right_id=len(cardPoints)-k
        hou=sum(cardPoints[-k:])
        dangqian = hou
        for i in range(k):
            dangqian = dangqian + cardPoints[left_id]-cardPoints[right_id]
            left_id+=1
            right_id+=1
            if dangqian > hou:
                hou = dangqian
        return hou
