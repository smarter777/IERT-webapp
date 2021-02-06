# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        经典解法就是用两个指针，一个跑得快，一个跑得慢。
        如果不含有环，跑得快的那个指针最终会遇到 null，说明链表不含环；
        如果含有环，快指针最终会超慢指针一圈，和慢指针相遇，说明链表含有环。
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
