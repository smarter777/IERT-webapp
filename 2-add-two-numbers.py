# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = []
        num2 = []
        cur_1 = l1
        while cur_1:
            num1.append(str(cur_1.val))
            cur_1 = cur_1.next
        cur_2 = l2
        while cur_2:
            num2.append(str(cur_2.val))
            cur_2 = cur_2.next
        sum_t = int("".join(num1[::-1])) + int("".join(num2[::-1]))
        sum_t = str(sum_t)[::-1]
        head = ListNode(int(sum_t[0]))
        cur = head
        for one in sum_t[1:]:
            cur.next = ListNode(val=int(one))
            cur = cur.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:return l1
        dummy = tmp = ListNode(None)
        s = 0
        while l1 or l2 or s:
            s = s + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            tmp.next = ListNode(s % 10)
            tmp = tmp.next
            s //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next