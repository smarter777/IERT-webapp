# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_head1 = ListNode()
        dummy_head2 = ListNode()
        prev1 = dummy_head1
        prev2 = dummy_head2

        cur = head
        while cur:
            if cur.val < x:
                prev1.next = cur
                cur = cur.next
                prev1 = prev1.next
                # prev1.next =None
            else:
                prev2.next = cur
                cur = cur.next
                prev2 = prev2.next
                prev2.next = None

        prev1.next = dummy_head2.next
        ret = dummy_head1.next

        return ret


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummyNode1 = l1 = ListNode(0)
        dummyNode2 = l2 = ListNode(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = dummyNode2.next
        return dummyNode1.next
