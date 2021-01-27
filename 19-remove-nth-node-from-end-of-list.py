# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next:
            return None
        cur = head
        cur_n = head
        for i in range(n):
            cur_n = cur_n.next
        if not cur_n:  # [1,2] 2
            return head.next
        while cur_n.next:
            cur = cur.next
            cur_n = cur_n.next
        # 此时的cur_n 指向最后一个元素，cur指向倒数第n个节点的前一个元素
        cur.next = cur.next.next

        return head