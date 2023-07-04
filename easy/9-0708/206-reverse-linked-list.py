class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            next_node = cur.next  # 2
            cur.next = prev  # 1 的next 等于 None
            prev = cur  # prev = 1
            cur = next_node  # 当前变成2
        return prev


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
