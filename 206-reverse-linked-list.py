class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            next = cur.next  # cur 不能为空
            cur.next = pre  # 反转已完成
            pre = cur  # 为下次做准备
            cur = next
        # cur 为空时跳出循环，pre 为原链表最后一个节点
        return pre

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p, rev = head, None
        while p:
            rev, rev.next, p = p, rev, p.next
        return rev