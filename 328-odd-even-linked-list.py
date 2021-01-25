# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy_head1 = ListNode()
        dummy_head2 = ListNode()
        prev1 = dummy_head1
        prev2 = dummy_head2

        cur = head
        i = 0
        while cur:
            if i % 2 == 0:
                prev1.next = cur
                cur = cur.next
                prev1 = prev1.next
                prev1.next = None
            else:
                prev2.next = cur
                cur = cur.next
                prev2 = prev2.next
                prev2.next = None

            i += 1

        prev1.next = dummy_head2.next
        ret = dummy_head1.next

        return ret


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        even = head
        odd_head = odd = head.next
        cur = head.next.next
        flag = True  # True为偶，False为奇
        while cur:
            if flag:
                even.next = cur
                even = even.next
            else:
                odd.next = cur
                odd = odd.next
            cur = cur.next
            flag = not flag

        even.next = odd_head
        odd.next = None
        return head
