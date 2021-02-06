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
        # 快指针先前进 n 步
        for i in range(n):
            cur_n = cur_n.next
        if not cur_n:  # [1,2] 2
            # 如果此时快指针走到头了
            # 说明倒数第 n 个节点就是第一个节点
            return head.next
        # 让慢指针和快指针同步向前
        while cur_n.next:
            cur = cur.next
            cur_n = cur_n.next
        # 此时的cur_n 指向最后一个元素，cur指向倒数第n个节点的前一个元素
        cur.next = cur.next.next

        return head

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