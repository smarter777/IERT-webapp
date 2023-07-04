class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 问题规模最小的解
        if head is None:
            return None
        res = self.removeElements(head.next, val)
        if head.val == val:
            return res
        else:
            head.next = res
            return head


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode()
        dummy_head.next = head
        prev = dummy_head
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy_head.next

