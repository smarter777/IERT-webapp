class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        作者：raptazure
        链接：https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/shuang-zhi-zhen-xu-ni-tou-jie-dian-python3-9420-fa/
        """
        if m == n:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        a, d = dummy, dummy
        for _ in range(m - 1):
            a = a.next
        for _ in range(n):
            d = d.next
        b, c = a.next, d.next
        pre = b
        cur = pre.next
        while cur != c:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        a.next = d
        b.next = c
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy_head = ListNode()
        dummy_head.next, superior = head, dummy_head
        # 遍历到m的前一个位置 superior (因为需要遍历到前一个位置, 所以最好创建一个虚拟头结点)
        for _ in range(m - 1): # 1. 遍历至m的前一个节点
            superior = superior.next
        # 定义一个节点使其指向m的位置 cur = superior.next
        # 然后就是按照反转链表1的方式直接套就好了. 需要注意一下循环的边界
        # 循环结束之后, 脑海中要浮现出三个指针的位置(浮现个屁, 用纸笔画一下吧骚年)
        # prev 指向n-m的位置,也就是最后一个旋转的节点 cur和next都指向n-m的下一个位置
        cur, prev = superior.next, None
        for _ in range(n - m + 1): # 2. 180°旋转爆炸
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        # 最后调整一下superior.next(m处的节点)和prev(n-m位置处)这两个节点的指向即可
        superior.next.next = cur #  3. 修改m和n-m位置处的节点的指向
        superior.next = prev
        return dummy_head.next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next:
            return head
        pre = None  # <m的部分
        rev = None  # 1<= m <= n 的部分,即需要翻转的部分
        pRev = None # 翻转链表中的首个节点，翻转完成以后就指向链表的最后一个节点，用于连接>n的剩余部分
        p = head
        count = 1
        while p:
            if count > n:   # >n以后不操作，直接链接（pre + rev + >n的部分节点）
                break
            if count >= m:  # 在翻转范围，对指定部分进行翻转
                tmp = p.next
                p.next = rev
                rev = p
                if not pRev:    # 翻转链表的指针，用于链接break以后剩余的链表，只需要指向第一个翻转节点，后续不重新赋值
                    pRev = rev
                p = tmp
            else:    # 当count > m以后，pre节点不需要再往后追踪，只追踪至开始翻转的节点的前一个节点即可
                pre = p
                p = p.next
            count += 1
        pRev.next = p   # 把翻转后的链表最后一个指针指向剩余head部分
        if pre: # 如果pre指针有值，则m>1，要把前中后三部分连接起来
            pre.next = rev
            return head
        else:   # 如果pre指针为空，则说明m = 1，一开始就要翻转，只需要返回中后部分，即rev + >n的部分，没有pre
            return rev