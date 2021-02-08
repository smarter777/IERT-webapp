

class Solution:
    """
    直接举个例子: k = 3

    pre
    tail    head
    dummy    1     2     3     4     5
    # 我们用tail 移到要翻转的部分最后一个元素
    pre     head       tail
    dummy    1     2     3     4     5
            cur
    # 我们尾插法的意思就是,依次把cur移到tail后面
    pre          tail  head
    dummy    2     3    1     4     5
            cur
    # 依次类推
    pre     tail      head
    dummy    3     2    1     4     5
            cur
    ....
    """

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        tail = dummy
        while True:
            count = k
            while count and tail:
                count -= 1
                tail = tail.next
            if not tail: break
            head = pre.next
            while pre.next != tail:
                cur = pre.next  # 获取下一个元素
                # pre与cur.next连接起来,此时cur(孤单)掉了出来
                pre.next = cur.next
                cur.next = tail.next  # 和剩余的链表连接起来
                tail.next = cur  # 插在tail后面
            # 改变 pre tail 的值
            pre = head
            tail = head
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/kge-yi-zu-fan-zhuan-lian-biao-by-powcai/
    """

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        while True:
            count = k
            stack = []
            tmp = head
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            # 注意,目前tmp所在k+1位置
            # 说明剩下的链表不够k个,跳出循环
            if count:
                p.next = head
                break
            # 翻转操作
            while stack:
                p.next = stack.pop()
                p = p.next
            # 与剩下链表连接起来
            p.next = tmp
            head = tmp

        return dummy.next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        tail = dummy
        while True:
            count = k
            while count and tail:
                count -= 1
                tail = tail.next
            if not tail: break
            head = pre.next
            while pre.next != tail:
                cur = pre.next  # 获取下一个元素
                # pre与cur.next连接起来,此时cur(孤单)掉了出来
                pre.next = cur.next
                cur.next = tail.next  # 和剩余的链表连接起来
                tail.next = cur  # 插在tail后面
            # 改变 pre tail 的值
            pre = head
            tail = head
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next
