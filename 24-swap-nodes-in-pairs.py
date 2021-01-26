# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode()
        dummy_head.next = head
        prev = dummy_head
        cur = head
        while cur and cur.next:
            first = cur
            second = cur.next
            third = cur.next.next

            prev.next = second  # cur = 1
            second.next = first  # next = 2 -> 1
            first.next = third  # prev = dummy

            prev = first
            cur = third
        return dummy_head.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        next_node = head.next
        head.next = self.swapPairs(next_node.next)
        next_node.next = head
        return next_node

