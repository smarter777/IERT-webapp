class Solution:
    """
    快指针一次前进两步，慢指针一次前进一步
    """
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

