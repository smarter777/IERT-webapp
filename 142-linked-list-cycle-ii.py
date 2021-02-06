class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        cur = head
        while cur and cur.next:
            if cur not in visited:
                visited.add(cur)
            else:
                return cur
            cur = cur.next
        return None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast  and fast.next:
            fast = fast.next.next
            slow = slow.next
            if (fast == slow):
                break
        # 上面的代码类似 hasCycle 函数
        if not fast or not fast.next:
            # fast 遇到空指针说明没有环
            return None
        slow = head;
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow